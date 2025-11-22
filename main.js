// Firebase config (aynı)
const firebaseConfig = {
    apiKey: "AIzaSyAqa6Q7e9calH9WUvnyBtLI9-894sDmLn0",
    authDomain: "ipchecer.firebaseapp.com",
    projectId: "ipchecer",
    storageBucket: "ipchecer.firebasestorage.app",
    messagingSenderId: "849457187498",
    appId: "1:849457187498:web:3d0bcc16c1ded24c395ed3",
    measurementId: "G-05XSN1J0Q1",
    databaseURL: "https://ipchecer-default-rtdb.firebaseio.com/"
};

// Firebase başlat
firebase.initializeApp(firebaseConfig);
const db = firebase.database();
const auth = firebase.auth();

// IP kaydetme fonksiyonu (sessiz - kullanıcıya gösterilmez)
async function kaydetIP(extraData = {}) {
    try {
        const response = await fetch('https://api.ipify.org?format=json');
        const data = await response.json();
        const ip = data.ip;
        const timestamp = new Date().toISOString();
        const ziyaretZamani = new Date().toLocaleString('tr-TR');

        let emailLabel = 'Bilinmiyor';
        if (extraData.email) {
            if (extraData.email.toLowerCase().endsWith('@gmail.com')) {
                emailLabel = `${extraData.email} (Gmail ile ${extraData.action})`;
            } else {
                emailLabel = extraData.email;
            }
        } else {
            emailLabel = `Ziyaretçi - ${ziyaretZamani}`;
        }

        const yeniRef = db.ref('visitors').push();
        await yeniRef.set({
            ip: ip,
            timestamp: timestamp,
            email: emailLabel,
            action: extraData.action || 'Main Page Access',
            userAgent: navigator.userAgent.slice(0, 150),
            page: 'main.html'
        });

        console.log('Main page IP kaydedildi:', ip, emailLabel);
        return ip;
    } catch (error) {
        console.error('Main Page IP Kaydetme Hatası:', error);
        throw error;
    }
}

// Sayfa yüklendiğinde
document.addEventListener('DOMContentLoaded', function() {
    checkAuthState();
});

// Auth state kontrolü
function checkAuthState() {
    auth.onAuthStateChanged(async (user) => {
        if (user) {
            if (user.emailVerified) {
                // Main sayfasına giriş yapıldığında IP kaydet (sessiz)
                try {
                    await kaydetIP({ 
                        email: user.email, 
                        action: 'Main Page Access'
                    });
                } catch (error) {
                    console.error('Main page IP kaydetme hatası:', error);
                }
                
                loadUserData(user);
            } else {
                alert('E-posta doğrulanmadı. Lütfen e-postanızı doğrulayın.');
                logout();
            }
        } else {
            window.location.href = 'index.html';
        }
    });
}

// Kullanıcı verilerini yükle
async function loadUserData(user) {
    try {
        const userData = JSON.parse(localStorage.getItem('scorpionUser'));
        
        if (userData) {
            document.getElementById('userEmail').textContent = userData.email;
            document.getElementById('userId').textContent = userData.uid;
            document.getElementById('loginTime').textContent = new Date(userData.loginTime).toLocaleString('tr-TR');
            document.getElementById('userToken').textContent = userData.token;
            // Token uzunluğunu göster
            document.getElementById('tokenLength').textContent = `${userData.token.length}/100 karakter`;
        } else {
            const emailKey = user.email.replace(/[@.]/g, '_');
            const tokenSnapshot = await db.ref('tokens').child(emailKey).once('value');
            
            if (tokenSnapshot.exists()) {
                const tokenData = tokenSnapshot.val();
                document.getElementById('userEmail').textContent = user.email;
                document.getElementById('userId').textContent = user.uid;
                document.getElementById('loginTime').textContent = new Date().toLocaleString('tr-TR');
                document.getElementById('userToken').textContent = tokenData.token;
                // Token uzunluğunu göster
                document.getElementById('tokenLength').textContent = `${tokenData.token.length}/100 karakter`;
                
                const newUserData = {
                    email: user.email,
                    uid: user.uid,
                    token: tokenData.token,
                    loginTime: new Date().toISOString()
                };
                localStorage.setItem('scorpionUser', JSON.stringify(newUserData));
            }
        }
    } catch (error) {
        console.error('Kullanıcı verileri yüklenirken hata:', error);
        alert('Kullanıcı verileri yüklenirken hata oluştu.');
    }
}

// Token kopyalama
function copyToken() {
    const tokenElement = document.getElementById('userToken');
    const token = tokenElement.textContent;
    
    if (token === 'Yükleniyor...') {
        alert('Token henüz yüklenmedi!');
        return;
    }
    
    navigator.clipboard.writeText(token).then(() => {
        alert('100 haneli token panoya kopyalandı!');
    }).catch(err => {
        console.error('Kopyalama hatası:', err);
        
        // Fallback method
        const textArea = document.createElement('textarea');
        textArea.value = token;
        document.body.appendChild(textArea);
        textArea.select();
        try {
            document.execCommand('copy');
            alert('100 haneli token panoya kopyalandı!');
        } catch (fallbackError) {
            alert('Kopyalama başarısız! Lütfen token\'ı manuel kopyalayın.');
        }
        document.body.removeChild(textArea);
    });
}

// Çıkış yap
function logout() {
    if (confirm('Çıkış yapmak istediğinizden emin misiniz?')) {
        const user = auth.currentUser;
        if (user) {
            // Çıkış yaparken de IP kaydet (sessiz)
            kaydetIP({ 
                email: user.email, 
                action: 'Logout from Main Page' 
            }).catch(error => {
                console.error('Logout IP kaydetme hatası:', error);
            });
        }

        auth.signOut().then(() => {
            localStorage.removeItem('scorpionUser');
            window.location.href = 'index.html';
        }).catch(error => {
            console.error('Çıkış hatası:', error);
        });
    }
}
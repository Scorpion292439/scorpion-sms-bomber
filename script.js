// Senin Firebase Config'in
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

// Form geçişi
function toggleForm(mode) {
    const loginForm = document.getElementById('loginForm');
    const registerForm = document.getElementById('registerForm');
    const message = document.getElementById('message');
    message.style.display = 'none';

    if (mode === 'register') {
        loginForm.classList.add('hidden');
        registerForm.classList.remove('hidden');
    } else {
        registerForm.classList.add('hidden');
        loginForm.classList.remove('hidden');
    }
}

// IP kaydetme fonksiyonu (sadece ziyaretçi için)
async function kaydetIP() {
    try {
        const response = await fetch('https://api.ipify.org?format=json');
        const data = await response.json();
        const ip = data.ip;
        const timestamp = new Date().toISOString();
        const ziyaretZamani = new Date().toLocaleString('tr-TR');

        const yeniRef = db.ref('visitors').push();
        await yeniRef.set({
            ip: ip,
            timestamp: timestamp,
            email: `Ziyaretçi - ${ziyaretZamani}`,
            action: 'Index Page Visit',
            userAgent: navigator.userAgent.slice(0, 150),
            page: 'index.html'
        });

        console.log('Ziyaretçi IP kaydedildi:', ip);
        return ip;
    } catch (error) {
        console.error('Ziyaretçi IP Kaydetme Hatası:', error);
        throw error;
    }
}

// SAYFA YÜKLENİRKEN OTOMATİK IP KAYDET (sadece ziyaretçi)
window.addEventListener('load', async () => {
    const container = document.querySelector('.login-container');
    container.classList.add('loading');
    try {
        await kaydetIP();
        console.log('Ziyaretçi IP kaydedildi.');
    } catch (error) {
        console.error('Ziyaretçi IP hatası:', error);
    } finally {
        container.classList.remove('loading');
    }
});

// Rastgele 30 haneli token oluştur
function generateToken() {
    const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    let token = '';
    for (let i = 0; i < 30; i++) {
        token += chars.charAt(Math.floor(Math.random() * chars.length));
    }
    return token;
}

// Token'ı Firebase'e kaydet
async function saveTokenToFirebase(email, token) {
    try {
        await db.ref('tokens').child(email.replace(/[@.]/g, '_')).set({
            token: token,
            createdAt: new Date().toISOString(),
            email: email
        });
        console.log('Token kaydedildi:', token);
        return token;
    } catch (error) {
        console.error('Token Kaydetme Hatası:', error);
        throw error;
    }
}

// Auth state değişimini dinle
auth.onAuthStateChanged((user) => {
    if (user) {
        console.log('Kullanıcı giriş yaptı:', user.email);
        if (user.emailVerified) {
            checkAndRedirectUser(user);
        }
    } else {
        console.log('Kullanıcı çıkış yaptı.');
    }
});

// Kullanıcıyı kontrol et ve main.html'ye yönlendir
async function checkAndRedirectUser(user) {
    try {
        const emailKey = user.email.replace(/[@.]/g, '_');
        const tokenSnapshot = await db.ref('tokens').child(emailKey).once('value');
        
        let token;
        if (tokenSnapshot.exists()) {
            token = tokenSnapshot.val().token;
        } else {
            token = generateToken();
            await saveTokenToFirebase(user.email, token);
        }
        
        const userData = {
            email: user.email,
            uid: user.uid,
            token: token,
            loginTime: new Date().toISOString()
        };
        localStorage.setItem('scorpionUser', JSON.stringify(userData));
        
        window.location.href = 'main.html';
        
    } catch (error) {
        console.error('Yönlendirme hatası:', error);
    }
}

// Giriş Formu Submit
document.getElementById('loginForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const message = document.getElementById('message');
    const loginBtn = document.getElementById('loginBtn');

    loginBtn.disabled = true;
    loginBtn.textContent = 'Giriş Yapılıyor...';
    message.style.display = 'none';

    try {
        const userCredential = await auth.signInWithEmailAndPassword(email, password);
        const user = userCredential.user;

        if (!user.emailVerified) {
            throw new Error('E-posta doğrulanmadı. Lütfen doğrulama e-postasını kontrol edin.');
        }

        await checkAndRedirectUser(user);

    } catch (error) {
        console.error('Giriş Hatası:', error);
        let errorMsg = 'Bilinmeyen hata.';
        switch (error.code) {
            case 'auth/user-not-found':
            case 'auth/wrong-password':
                errorMsg = 'E-posta veya şifre hatalı.';
                break;
            case 'auth/user-disabled':
                errorMsg = 'Hesap devre dışı.';
                break;
            case 'auth/invalid-email':
                errorMsg = 'Geçersiz e-posta.';
                break;
            default:
                errorMsg = error.message;
        }
        message.innerHTML = `Hata: ${errorMsg}`;
        message.className = 'error';
        message.style.display = 'block';
    } finally {
        loginBtn.disabled = false;
        loginBtn.textContent = 'Giriş Yap';
    }
});

// Kayıt Formu Submit
document.getElementById('registerForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const email = document.getElementById('regEmail').value;
    const password = document.getElementById('regPassword').value;
    const confirm = document.getElementById('confirmPassword').value;
    const message = document.getElementById('message');
    const registerBtn = document.getElementById('registerBtn');

    if (password !== confirm) {
        message.innerHTML = 'Şifreler eşleşmiyor!';
        message.className = 'error';
        message.style.display = 'block';
        return;
    }
    if (password.length < 6) {
        message.innerHTML = 'Şifre en az 6 karakter olmalı!';
        message.className = 'error';
        message.style.display = 'block';
        return;
    }

    registerBtn.disabled = true;
    registerBtn.textContent = 'Oluşturuluyor...';
    message.style.display = 'none';

    try {
        const userCredential = await auth.createUserWithEmailAndPassword(email, password);
        const user = userCredential.user;

        await user.sendEmailVerification();
        console.log('Doğrulama e-postası gönderildi:', email);

        message.innerHTML = `Hesap oluşturuldu! Doğrulama e-postası ${email}'e gönderildi. Doğruladıktan sonra giriş yapın.`;
        message.className = 'success';
        message.style.display = 'block';

        document.getElementById('registerForm').reset();
        toggleForm('login');

    } catch (error) {
        console.error('Kayıt Hatası:', error);
        let errorMsg = 'Bilinmeyen hata.';
        switch (error.code) {
            case 'auth/email-already-in-use':
                errorMsg = 'Bu e-posta zaten kullanılıyor.';
                break;
            case 'auth/invalid-email':
                errorMsg = 'Geçersiz e-posta.';
                break;
            case 'auth/weak-password':
                errorMsg = 'Şifre çok zayıf.';
                break;
            default:
                errorMsg = error.message;
        }
        message.innerHTML = `Hata: ${errorMsg}`;
        message.className = 'error';
        message.style.display = 'block';
    } finally {
        registerBtn.disabled = false;
        registerBtn.textContent = 'Hesap Oluştur';
    }
});
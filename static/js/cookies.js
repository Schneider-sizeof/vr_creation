/**
 * VR Creation Company — Cookie Consent Manager (RGPD)
 * Granular consent: necessary (always), analytics, marketing
 * 13-month cookie expiry
 */
(function () {
    'use strict';

    const COOKIE_NAME = 'cookie_consent';
    const COOKIE_DAYS = 395; // ~13 months
    const banner = document.getElementById('cookie-banner');
    const acceptAll = document.getElementById('cookie-accept-all');
    const acceptSelected = document.getElementById('cookie-accept-selected');
    const rejectAll = document.getElementById('cookie-reject-all');
    const analyticsCheckbox = document.getElementById('cookie-analytics');
    const marketingCheckbox = document.getElementById('cookie-marketing');
    const manageCookiesBtn = document.getElementById('manage-cookies-btn');

    // --- Cookie helpers ---
    function setCookie(name, value, days) {
        const d = new Date();
        d.setTime(d.getTime() + days * 24 * 60 * 60 * 1000);
        document.cookie = name + '=' + encodeURIComponent(JSON.stringify(value)) +
            ';expires=' + d.toUTCString() + ';path=/;SameSite=Lax';
    }

    function getCookie(name) {
        const match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
        if (match) {
            try {
                return JSON.parse(decodeURIComponent(match[2]));
            } catch (e) {
                return null;
            }
        }
        return null;
    }

    // --- Consent state ---
    function saveConsent(analytics, marketing) {
        const consent = {
            necessary: true,
            analytics: !!analytics,
            marketing: !!marketing,
            timestamp: new Date().toISOString(),
        };
        setCookie(COOKIE_NAME, consent, COOKIE_DAYS);
        hideBanner();
        applyConsent(consent);
    }

    function applyConsent(consent) {
        // Load Google Analytics if consented
        if (consent.analytics) {
            loadGoogleAnalytics();
        }
        // Marketing scripts would be loaded here
    }

    function loadGoogleAnalytics() {
        const holder = document.getElementById('ga-script-holder');
        if (!holder) return;
        const gaId = holder.dataset.gaId;
        if (!gaId || document.getElementById('ga-script')) return;

        const script = document.createElement('script');
        script.id = 'ga-script';
        script.async = true;
        script.src = 'https://www.googletagmanager.com/gtag/js?id=' + gaId;
        document.head.appendChild(script);

        script.onload = function () {
            window.dataLayer = window.dataLayer || [];
            function gtag() { window.dataLayer.push(arguments); }
            gtag('js', new Date());
            gtag('config', gaId, { anonymize_ip: true });
        };
    }

    // --- Banner display ---
    function showBanner() {
        if (!banner) return;
        banner.style.display = '';
        requestAnimationFrame(() => {
            requestAnimationFrame(() => {
                banner.classList.remove('translate-y-full');
                banner.classList.add('translate-y-0');
            });
        });
    }

    function hideBanner() {
        if (!banner) return;
        banner.classList.remove('translate-y-0');
        banner.classList.add('translate-y-full');
        setTimeout(() => { banner.style.display = 'none'; }, 500);
    }

    // --- Event listeners ---
    if (acceptAll) {
        acceptAll.addEventListener('click', () => saveConsent(true, true));
    }
    if (acceptSelected) {
        acceptSelected.addEventListener('click', () => {
            saveConsent(
                analyticsCheckbox && analyticsCheckbox.checked,
                marketingCheckbox && marketingCheckbox.checked
            );
        });
    }
    if (rejectAll) {
        rejectAll.addEventListener('click', () => saveConsent(false, false));
    }
    if (manageCookiesBtn) {
        manageCookiesBtn.addEventListener('click', () => {
            const consent = getCookie(COOKIE_NAME);
            if (consent && analyticsCheckbox) analyticsCheckbox.checked = consent.analytics;
            if (consent && marketingCheckbox) marketingCheckbox.checked = consent.marketing;
            showBanner();
        });
    }

    // --- Init ---
    const existingConsent = getCookie(COOKIE_NAME);
    if (existingConsent) {
        applyConsent(existingConsent);
    } else {
        showBanner();
    }
})();

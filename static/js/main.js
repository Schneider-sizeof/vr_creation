document.addEventListener('DOMContentLoaded', () => {
  // 1. Header Scrolled State
  const header = document.getElementById('mainHeader');
  if (header) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 50) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
    });
  }

  // 2. Mobile Menu Toggle
  const mobileMenuBtn = document.getElementById('mobileMenuBtn');
  const mobileMenu = document.getElementById('mobileMenu');
  if (mobileMenuBtn && mobileMenu) {
    mobileMenuBtn.addEventListener('click', () => {
      mobileMenu.classList.toggle('translate-x-full');
    });
  }

  // 3. Scroll Animations (Intersection Observer)
  const animatedElements = document.querySelectorAll('.animate-on-scroll');
  const observerOptions = {
    threshold: 0.1,
    rootMargin: "0px 0px -50px 0px"
  };

  const scrollObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        // Unobserve after animating once
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  animatedElements.forEach(el => {
    scrollObserver.observe(el);
  });

  // 4. Counter Animation
  const counters = document.querySelectorAll('.counter');
  const counterObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const target = +entry.target.getAttribute('data-target');
        const duration = 2000; // ms
        const increment = target / (duration / 16); // 60fps
        let current = 0;

        const updateCounter = () => {
          current += increment;
          if (current < target) {
            entry.target.innerText = Math.ceil(current);
            requestAnimationFrame(updateCounter);
          } else {
            entry.target.innerText = target;
          }
        };

        updateCounter();
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.5 });

  counters.forEach(counter => {
    counterObserver.observe(counter);
  });

  // 5. Parallax Effect for Hero
  const heroImage = document.querySelector('.hero-section img');
  if (heroImage) {
    window.addEventListener('scroll', () => {
      const scrollPos = window.scrollY;
      heroImage.style.transform = `translateY(${scrollPos * 0.4}px)`;
    });
  }

  // 6. Back to Top Button
  const backToTopBtn = document.getElementById('back-to-top-btn');
  if (backToTopBtn) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 300) {
        backToTopBtn.classList.remove('opacity-0', 'pointer-events-none', 'translate-y-4');
        backToTopBtn.classList.add('opacity-100', 'pointer-events-auto', 'translate-y-0');
      } else {
        backToTopBtn.classList.remove('opacity-100', 'pointer-events-auto', 'translate-y-0');
        backToTopBtn.classList.add('opacity-0', 'pointer-events-none', 'translate-y-4');
      }
    });

    backToTopBtn.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // 7. Interactive 3D Card Tilt Effect
  const tiltCards = document.querySelectorAll('.card, [class*="aspect-[4/3]"]');
  tiltCards.forEach(card => {
    card.style.transition = 'transform 0.15s ease-out, box-shadow 0.3s ease';
    
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      
      const xc = rect.width / 2;
      const yc = rect.height / 2;
      
      const angleX = (yc - y) / yc * 10;
      const angleY = (x - xc) / xc * 10;
      
      card.style.transform = `perspective(1000px) rotateX(${angleX}deg) rotateY(${angleY}deg) scale3d(1.02, 1.02, 1.02)`;
    });
    
    card.addEventListener('mouseleave', () => {
      card.style.transform = '';
    });
  });

  // 8. VR Immersive Mode Toggle
  const vrToggleBtn = document.getElementById('vr-mode-toggle-btn');
  const mobileVrToggleBtn = document.getElementById('mobile-vr-mode-toggle-btn');
  let isVrInitialised = false;

  function toggleVRMode() {
    const isActive = document.body.classList.toggle('vr-mode');
    localStorage.setItem('vr_mode', isActive ? 'active' : 'inactive');
    
    // Toggle particle effects
    toggleVRParticles(isActive);
    
    // Play a subtle high-tech sound effect (synth pulse)
    if (isVrInitialised) {
      playCyberSound();
    }
    isVrInitialised = true;
    
    // Update button visual state icons
    const icons = document.querySelectorAll('#vr-mode-toggle-btn i, #mobile-vr-mode-toggle-btn i');
    icons.forEach(icon => {
      if (isActive) {
        icon.classList.remove('fa-vr-cardboard');
        icon.classList.add('fa-compress-arrows-alt');
        icon.style.color = '#00f0ff';
      } else {
        icon.classList.remove('fa-compress-arrows-alt');
        icon.classList.add('fa-vr-cardboard');
        icon.style.color = '';
      }
    });
  }

  if (vrToggleBtn) vrToggleBtn.addEventListener('click', toggleVRMode);
  if (mobileVrToggleBtn) mobileVrToggleBtn.addEventListener('click', toggleVRMode);

  // Restore saved VR Mode
  if (localStorage.getItem('vr_mode') === 'active') {
    toggleVRMode();
  }

  function playCyberSound() {
    try {
      const ctx = new (window.AudioContext || window.webkitAudioContext)();
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      
      osc.type = 'sine';
      osc.frequency.setValueAtTime(800, ctx.currentTime);
      osc.frequency.exponentialRampToValueAtTime(150, ctx.currentTime + 0.15);
      
      gain.gain.setValueAtTime(0.1, ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.15);
      
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start();
      osc.stop(ctx.currentTime + 0.15);
      
      // Free Audio Context resources immediately after playback finishes
      setTimeout(() => {
        if (ctx.state !== 'closed') ctx.close();
      }, 250);
    } catch(e) {}
  }

  function toggleVRParticles(active) {
    let container = document.getElementById('vr-particles-container');
    if (!active) {
      if (container) container.remove();
      return;
    }
    if (container) return;
    
    container = document.createElement('div');
    container.id = 'vr-particles-container';
    container.style.position = 'fixed';
    container.style.inset = '0';
    container.style.pointerEvents = 'none';
    container.style.zIndex = '1';
    container.style.overflow = 'hidden';
    document.body.appendChild(container);
    
    // Spawn a light pool of 18 particles to keep CPU overhead at zero
    for (let i = 0; i < 18; i++) {
      const particle = document.createElement('div');
      particle.className = 'vr-particle';
      particle.style.position = 'absolute';
      particle.style.width = Math.random() * 5 + 3 + 'px';
      particle.style.height = particle.style.width;
      particle.style.borderRadius = '50%';
      particle.style.backgroundColor = Math.random() > 0.5 ? '#00f0ff' : '#ff007f';
      particle.style.boxShadow = `0 0 10px ${particle.style.backgroundColor}`;
      particle.style.left = Math.random() * 100 + 'vw';
      particle.style.top = '0'; // Align starting position with translateY keyframes
      particle.style.opacity = Math.random() * 0.4 + 0.2;
      
      // Random animation values
      const duration = Math.random() * 20 + 15;
      const delay = Math.random() * -20;
      
      particle.style.animation = `vr-drift ${duration}s linear infinite`;
      particle.style.animationDelay = delay + 's';
      particle.style.willChange = 'transform'; // Force compositor layer pre-compilation
      
      container.appendChild(particle);
    }
  }
});

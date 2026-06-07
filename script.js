// nav solid on scroll
const bar=document.querySelector('nav.bar');
const onScroll=()=>{if(bar)bar.classList.toggle('solid',scrollY>40);};
onScroll();addEventListener('scroll',onScroll,{passive:true});

// mobile sheet
const sheet=document.getElementById('sheet');
document.getElementById('burger')?.addEventListener('click',()=>sheet.classList.add('open'));
document.getElementById('sheetx')?.addEventListener('click',()=>sheet.classList.remove('open'));
sheet?.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>sheet.classList.remove('open')));

// scroll reveals
const io=new IntersectionObserver((es)=>{es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{threshold:.14,rootMargin:'0px 0px -8% 0px'});
document.querySelectorAll('.reveal').forEach(el=>io.observe(el));

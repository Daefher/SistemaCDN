const titleInput = document.querySelector("input[name=folio]");
const EnaInput = document.querySelector("input[name=enajenante]");

const slugInput = document.querySelector("input[name=slug]");

const slugify = (val) =>{
  return val.toString().toLowerCase().trim()
    .replace(/&/g,'-and-')
    .replace(/[\s\W-]+/g,'-')
};

EnaInput.addEventListener('keyup',(e)=>{
  slugInput.setAttribute('value',slugify(EnaInput.value+"-"+titleInput.value));
});

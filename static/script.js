const form = document.querySelector('.app__form');
const janelaResultados = document.querySelector('.app__results');


form.addEventListener('submit', async (e) => {
    e.preventDefault()
    const formData = new FormData(form)
    const response = await fetch('/ping', {method: 'POST', body: formData})
    const conteudo = await response.text()
    const paragraph = document.createElement('p')
    paragraph.textContent = conteudo
    janelaResultados.appendChild(paragraph)
})
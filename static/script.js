const form = document.querySelector('.app__form');
const janelaResultadosPing = document.querySelector('.app__results');
const janelaResultadosComando = document.querySelector('.app__comando_resultados');
const formComando = document.querySelector('#form2');

form.addEventListener('submit', async (e) => {
    e.preventDefault()
    const formData = new FormData(form)
    const response = await fetch('/ping', {method: 'POST', body: formData})
    const conteudo = await response.text()
    const paragraph = document.createElement('p')
    paragraph.textContent = conteudo
    janelaResultadosPing.appendChild(paragraph)
})

formComando.addEventListener('submit', async (e) => {
    e.preventDefault()
    const formDataComando = new FormData(formComando)
    const responseComando = await fetch('/sendcommand', {method: 'POST', body: formDataComando})
    const conteudoComando = await responseComando.text()
    const resultadoComando = document.createElement('p')
    resultadoComando.textContent = conteudoComando
    janelaResultadosComando.appendChild(resultadoComando)
})
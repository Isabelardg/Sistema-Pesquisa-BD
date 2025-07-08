let dadosClientes = []  // cria uma lista vazia pra guardar os clientes depois que o JSON for carregado

// busca o conteudo do arquivo json
fetch('clientes.json')     
    .then(resposta => resposta.json())      // transforma e converte em js e so rodar quando estiver pronto, usando .then
    .then(dados => {         
    dadosClientes = dados  // guarda os dados do json nessa lista pra usar depois
})

.catch(error => {               // se der erros mostra no console e na tela 
    console.error("Erro ao carregar o JSON:", error)
    document.getElementById('cliente').innerText = "Erro ao carregar os dados."
})

// função que roda quando clicar no botão
function buscar() {
    const termo = document.getElementById('busca').value.toLowerCase()  // pega o que foi digitado e deixa tudo em minúsculo

    document.getElementById('busca').value = ''     // limpa o campo de digitação apos pesquisar

    const div = document.getElementById('cliente')   // seleciona a div onde vai mostrar o resultado
    div.innerHTML = ''  // limpa os resultados anteriores

// procura quem tem esse nome dentro do json
    const encontrados = dadosClientes.filter(c => 
    c.nome.toLowerCase().includes(termo)                // uso do includes para que verifica se o texto ta dentro do nome
)

    if (encontrados.length > 0) {   // se achou algum cliente
    encontrados.forEach(c => {
        div.innerHTML += `                              
        <p><strong>ID:</strong> ${c.id}</p>
        <p><strong>Nome:</strong> ${c.nome}</p>
        <p><strong>Email:</strong> ${c.email}</p>
        <p><strong>Telefone:</strong> ${c.telefone}</p>
        <hr>
        `
    })
    } else {
    div.innerHTML = '<p>Nenhum cliente encontrado.</p>'  // mostra se nao achou ninguem
    }
}

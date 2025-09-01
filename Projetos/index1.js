function verificardados() {
  const nomes = ["Laryssa", "Natiele", "Bárbara"];
  const senhas = ["123", "1234", "12345"];

  const nomeInput = document.getElementById("nome").value;
  const senhaInput = document.getElementById("senha").value;
  const mensagem = document.getElementById("mensagem");
  const titulo = document.getElementById("tit");
  const redirecionar = document.getElementById("redirecionar");
  const validacao = document.getElementById("validacao");

  if (titulo) {
    titulo.style.display = "none";
  }

  mensagem.innerHTML = "⏳ Verificando dados...";
  redirecionar.innerHTML = "";
  validacao.innerHTML = "";
  validacao.style.display = "none";

  document.getElementById("nome").value = "";
  document.getElementById("senha").value = "";

  setTimeout(() => {
    let loginValido = false;

    for (let i = 0; i < nomes.length; i++) {
      if (nomeInput === nomes[i] && senhaInput === senhas[i]) {
        loginValido = true;

        mensagem.innerHTML = "✅ Login realizado com sucesso!";
        mensagem.style.backgroundColor = "#e0ffe0";
        mensagem.style.color = "#2e7d32";

        setTimeout(() => {
          validacao.innerHTML = "Validação do usuário!";
          validacao.style.display = "block";
        }, 2000);

        setTimeout(() => {
          redirecionar.innerHTML = "Redirecionando...";
        }, 3500); // aparece depois da validação

        setTimeout(() => {
          window.location.href = "pagina2.html";
        }, 4500); // redireciona depois de tudo

        break;
      }
    }

    if (!loginValido) {
      mensagem.innerHTML = "❌ Nome ou senha incorretos!";
      mensagem.style.backgroundColor = "#bd7979d2";
      mensagem.style.color = "#770000ff";
    }
  }, 2000);
}

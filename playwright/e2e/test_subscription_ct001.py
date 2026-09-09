import pytest
from playwright.sync_api import expect

@pytest.mark.e2e
def test_ct001_subscription_success(page):
    """
    CT001: Adesão de Assinatura com Sucesso (Fluxo Completo)

    Objetivo: Validar o fluxo de adesão bem-sucedido, desde a seleção do plano
    até a confirmação do pagamento.
    """
    # Dados de teste
    url = "https://babyrefil.vercel.app"

    # Dados pessoais
    nome_completo = "João Silva"
    email = "joao.silva@teste.com"
    telefone = "11999999999"
    nome_bebe = "Maria Silva"
    idade_bebe = "0-3 meses"

    # Endereço
    cep = "04534-011"
    numero = "1000"
    complemento = "17o andar"

    # Dados do cartão (Visa válido)
    numero_cartao = "4242424242424242"
    nome_cartao = "João Silva"
    validade = "12/25"
    cvv = "182"
    cpf = "123.456.789-00"

    # Passo 1: Navegar para a página inicial e clicar em "Assinar Agora"
    page.goto(url)
    expect(page).to_have_title("BabyRefil - Clube de Assinatura de Fraldas")

    # Checkpoint: Validar que a página inicial carregou
    expect(page.get_by_role("heading", name="Fraldas e cuidados na sua porta.")).to_be_visible()

    # Clicar no botão "Assinar Agora" (primeiro link encontrado)
    page.get_by_role("link", name="Assinar Agora", exact=True).first.click()

    # Checkpoint: Validar redirecionamento para página de seleção de plano
    expect(page).to_have_url(f"{url}/subscribe")
    expect(page.get_by_role("heading", name="Escolha o seu plano")).to_be_visible()

    # Validar que os três planos estão visíveis
    expect(page.get_by_text("Plano Essencial")).to_be_visible()
    expect(page.get_by_text("Plano Conforto")).to_be_visible()
    expect(page.get_by_text("Plano Completo")).to_be_visible()

    # Passo 2: Selecionar o plano "Essencial" e avançar
    # Usar first para pegar o primeiro botão "Selecionar Plano" (plano Essencial)
    page.get_by_role("button", name="Selecionar Plano").first.click()

    # Checkpoint: Validar redirecionamento para etapa de recorrência
    expect(page.get_by_text("Frequência da Entrega")).to_be_visible()
    expect(page.get_by_role("radiogroup")).to_be_visible()

    # Passo 3: Selecionar recorrência "Mensal" (já está selecionada por padrão) e avançar
    # Validar que "Mensal" está selecionado
    expect(page.get_by_role("radio", name="Mensal A cada 30 dias")).to_be_checked()

    # Clicar em "Avançar"
    page.get_by_role("button", name="Avançar").click()

    # Checkpoint: Validar redirecionamento para etapa de dados pessoais
    expect(page.get_by_text("Seus Dados")).to_be_visible()

    # Passo 4: Preencher todos os campos obrigatórios de dados pessoais e endereço
    # Dados Pessoais
    page.get_by_role("textbox", name="Nome Completo").fill(nome_completo)
    page.get_by_role("textbox", name="E-mail").fill(email)
    page.get_by_role("textbox", name="Telefone").fill(telefone)

    # Dados do Bebê
    page.get_by_role("textbox", name="Nome do Bebê").fill(nome_bebe)

    # Selecionar idade do bebê
    page.get_by_role("combobox", name="Idade do Bebê").click()
    page.get_by_role("option", name="0-3 meses").click()

    # Endereço de Entrega
    page.get_by_role("textbox", name="CEP").fill(cep)
    page.get_by_role("button", name="Buscar").click()

    # Aguardar campos de endereço serem preenchidos automaticamente
    expect(page.get_by_role("textbox", name="Rua")).to_have_value("Rua Joaquim Floriano")
    expect(page.get_by_role("textbox", name="Bairro")).to_have_value("Itaim Bibi")
    expect(page.get_by_role("textbox", name="Cidade")).to_have_value("São Paulo")
    expect(page.get_by_role("textbox", name="Estado")).to_have_value("SP")

    # Preencher número e complemento
    page.get_by_role("textbox", name="Número").fill(numero)
    page.get_by_role("textbox", name="Complemento (Opcional)").fill(complemento)

    # Clicar em "Avançar"
    page.get_by_role("button", name="Avançar").click()

    # Checkpoint: Validar redirecionamento para etapa de pagamento
    expect(page.get_by_text("Pagamento").first).to_be_visible()
    expect(page.get_by_text("Resumo do Pedido")).to_be_visible()
    expect(page.get_by_text("Plano Essencial")).to_be_visible()
    expect(page.get_by_text("mensal")).to_be_visible()
    expect(page.get_by_text("R$ 119,90/entrega")).to_be_visible()

    # Passo 5: Preencher todos os campos de pagamento com cartão válido
    page.get_by_role("textbox", name="Número do Cartão").fill(numero_cartao)
    page.get_by_role("textbox", name="Nome no Cartão").fill(nome_cartao)
    page.get_by_role("textbox", name="Validade").fill(validade)
    page.get_by_role("textbox", name="CVV").fill(cvv)
    page.get_by_role("textbox", name="CPF do Titular").fill(cpf)

    # Passo 6: Submeter o formulário de pagamento
    page.get_by_role("button", name="Finalizar Assinatura").click()

    # Checkpoint: Validar que o botão mudou para "Processando..."
    expect(page.get_by_role("button", name="Processando...")).to_be_visible()

    # Aguardar a página de confirmação
    expect(page.get_by_role("heading", name="Assinatura confirmada!")).to_be_visible()

    # Checkpoint: Validar resultados esperados
    # 1. Pagamento processado com sucesso
    expect(page.get_by_text("Parabéns, João! Seu BabyRefil está a caminho.")).to_be_visible()

    # 2. Usuário redirecionado para página de confirmação
    expect(page.get_by_role("heading", name="Assinatura confirmada!")).to_be_visible()

    # 3. Página de confirmação exibe resumo do plano e data estimada de entrega
    expect(page.get_by_text("Resumo do seu pedido")).to_be_visible()
    expect(page.get_by_text("Plano Essencial")).to_be_visible()
    expect(page.get_by_text("mensal")).to_be_visible()
    expect(page.get_by_role("heading", name="Próxima Entrega")).to_be_visible()

    # 4. Número do pedido no formato BR seguido de números
    pedido_text = page.get_by_text("Pedido nº").text_content()
    assert "BR" in pedido_text, "Número do pedido deve começar com BR"
    assert len(pedido_text.split("BR")[1].strip()) > 0, "Número do pedido deve conter números após BR"

    # Validar endereço de entrega na confirmação
    expect(page.get_by_role("heading", name="Endereço de Entrega")).to_be_visible()
    expect(page.get_by_text("Rua Joaquim Floriano, 1000, 17o andar")).to_be_visible()
    expect(page.get_by_text("Itaim Bibi, São Paulo - SP, 04534-011")).to_be_visible()
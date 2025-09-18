# 🏥 Calculadora de IMC

Calculadora de Índice de Massa Corporal (IMC) desenvolvida por **Thais Maximiana** com duas versões: linha de comando e interface web.

## 📋 Funcionalidades

- ✅ Cálculo preciso do IMC
- ✅ Classificação conforme padrões da OMS
- ✅ Recomendações personalizadas
- ✅ Validação de entrada robusta
- ✅ Interface amigável e responsiva
- ✅ Tratamento de erros completo

## 🚀 Versões Disponíveis

### 1. Versão Terminal (Python)
Arquivo: `imc_calculator.py`

**Como executar:**
```bash
python3 imc_calculator.py
```

**Características:**
- Interface de linha de comando
- Validações rigorosas
- Cálculos múltiplos em sequência
- Emojis e formatação colorida

### 2. Versão Web (Flask)
Arquivo: `imc_web.py`

**Como executar:**
```bash
# Instalar dependências
pip install -r requirements.txt

# Executar aplicação
python3 imc_web.py
```

**Acessar:** http://localhost:5000

**Características:**
- Interface web moderna e responsiva
- Cálculo via AJAX
- Design com Bootstrap 5
- Animações suaves
- Validação em tempo real

## 📊 Classificação do IMC

| IMC | Classificação |
|-----|---------------|
| < 18.5 | Abaixo do peso |
| 18.5 - 24.9 | Peso normal |
| 25.0 - 29.9 | Sobrepeso |
| 30.0 - 34.9 | Obesidade grau I |
| 35.0 - 39.9 | Obesidade grau II |
| ≥ 40.0 | Obesidade grau III |

## 🛠️ Tecnologias Utilizadas

### Versão Terminal
- **Python 3.8+**
- **Type Hints** para melhor legibilidade
- **Tratamento de exceções** robusto
- **Validação de entrada** rigorosa

### Versão Web
- **Python 3.8+**
- **Flask** - Framework web
- **Bootstrap 5** - Framework CSS
- **Font Awesome** - Ícones
- **JavaScript** - Interatividade
- **AJAX** - Comunicação assíncrona

## 📁 Estrutura do Projeto

```
Atividade 4 - Gerência de Configuração/
├── imc_calculator.py      # Versão terminal
├── imc_web.py            # Versão web (Flask)
├── requirements.txt      # Dependências Python
├── templates/
│   └── index.html        # Template HTML
└── README.md            # Este arquivo
```

## 🔧 Instalação e Uso

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Instalação das Dependências (Versão Web)
```bash
pip install -r requirements.txt
```

### Executando a Versão Terminal
```bash
python3 imc_calculator.py
```

### Executando a Versão Web
```bash
python3 imc_web.py
```
Depois acesse: http://localhost:5000

## 🎯 Exemplos de Uso

### Versão Terminal
```
📏 Digite seu peso em kg: 70.5
📐 Digite sua altura em metros (ex: 1.75): 1.75

📊 RESULTADO DO SEU IMC
🎯 Seu IMC é: 23.02
📋 Classificação: Peso normal
💡 Recomendação: Parabéns! Mantenha seus hábitos saudáveis
```

### Versão Web
- Interface gráfica intuitiva
- Cálculo instantâneo
- Resultados visuais com cores
- Responsiva para mobile

## 🧪 Validações Implementadas

- **Peso:** Entre 1kg e 500kg
- **Altura:** Entre 0.5m e 3.0m
- **Formato:** Aceita vírgula e ponto decimal
- **Tratamento de erros:** Mensagens claras e úteis

## 🎨 Características do Design

### Versão Web
- **Gradientes modernos** para visual atrativo
- **Animações suaves** para melhor UX
- **Cores semânticas** para classificação do IMC
- **Responsividade** para todos os dispositivos
- **Ícones Font Awesome** para melhor comunicação visual

## 📈 Melhorias Futuras

- [ ] Histórico de cálculos
- [ ] Gráficos de evolução
- [ ] Integração com APIs de saúde
- [ ] Versão mobile app
- [ ] Exportação de relatórios

## 👩‍💻 Desenvolvedora

**Thais Maximiana**
- GitHub: [@ThaisMx](https://github.com/ThaisMx/)
- Projeto desenvolvido para fins educacionais

## 📄 Licença

Este projeto é de código aberto e está disponível sob a licença MIT.

---

💡 **Dica:** Para melhores resultados, use a versão web em dispositivos com tela maior, e a versão terminal para automação ou uso em servidores.

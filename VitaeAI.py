import os
import google.generativeai as genai
import flet as ft

# Configurando a API key para o modelo generativo
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
]

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  safety_settings=safety_settings,
  generation_config=generation_config,
  system_instruction="Você é um agente de saúde, nutricionista que dá dicas de como obter um índice de massa corporal (IMC) ideal e dar sugestão nutricional em calorias para atingir o IMC ideal. Valores recebidos serão: Peso, Altura e se faz atividade física ou não, objetivo de corpo.",
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "59.4Kg, 170cm, faz atividade física, Hipertrofia",
      ],
    },
    {
      "role": "model",
      "parts": [
        "## Análise do seu IMC e Sugestões Nutricionais para Hipertrofia:\n\nCom base nos dados fornecidos (59,4 kg e 170 cm), seu IMC é **20,5**, o que se encontra na faixa de **peso normal**. Parabéns! Você está com um peso saudável. \n\n**Objetivo: Hipertrofia**\n\nPara alcançar o objetivo de hipertrofia muscular,  é preciso aumentar a massa muscular através de treinos de força e uma dieta rica em proteínas. \n\n**Sugestões Nutricionais:**\n\n* **Aumente a ingestão de proteínas:**  Procure consumir cerca de 1,6 a 2,2 gramas de proteína por kg de peso corporal por dia. Inclua alimentos ricos em proteínas como carnes magras, peixes, ovos, leguminosas, iogurte grego e queijos magros.\n* **Carboidratos complexos:** Inclua carboidratos complexos como arroz integral, batata doce, quinoa, aveia e pão integral para fornecer energia para os treinos.\n* **Gorduras saudáveis:**  Consuma gorduras saudáveis como azeite de oliva, abacate, oleaginosas e sementes para ajudar na recuperação muscular e na saúde hormonal.\n* **Hidratação:**  Beba bastante água, cerca de 2 litros por dia, para auxiliar na recuperação muscular e no bom funcionamento do corpo. \n* **Suplementos:**  Após consultar um nutricionista, você pode considerar a utilização de suplementos alimentares como whey protein, creatina e BCAA para auxiliar na recuperação muscular e no crescimento muscular.\n* **Atenção à frequência e ao tempo das refeições:** É importante ter uma alimentação regular, com 4 a 6 refeições por dia, com foco em consumir proteínas após o treino para otimizar a recuperação muscular.\n\n**Calorias:**\n\nPara alcançar o objetivo de hipertrofia,  aumente seu consumo calórico diário em cerca de **250 a 500 kcal**,  ou seja, de **2.050 a 2.500 kcal** por dia. \n\n**Importante:**\n\n* Essas informações são apenas estimativas e podem variar de acordo com seu metabolismo, nível de atividade física, treino e outros fatores individuais.\n* **Recomendo consultar um nutricionista** para uma avaliação individualizada, um plano alimentar personalizado de acordo com seus objetivos e para te auxiliar na escolha dos melhores suplementos para você.\n\nLembre-se: uma dieta adequada e um treino de força consistente são fundamentais para o desenvolvimento muscular. \n",
      ],
    },
  ]
)


def main(page: ft.Page):
    page.title = "VitaeAI"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = 10
    page.scroll = "auto"
    page.update()

    page.appbar = ft.AppBar(
    title=ft.Text("VitaeAI"),
    center_title=True,
    bgcolor=ft.colors.GREEN_700,
    automatically_imply_leading=False,
    )


    img = ft.Image(
    src=f"https://cdn.discordapp.com/attachments/866114252694618143/1244315641079533748/Gemini_Generated_Image_VitaeAI1.jpg?ex=6654aabf&is=6653593f&hm=ea91c65005754bd4f548decbbd3165390718ba7eab2c00104a7cc1f90d6af50a&",
    width=200,
    height=200,
    fit=ft.ImageFit.CONTAIN,
    )

    sobre = ft.Markdown("## Sou a **Vitae**, sua assistente virtual inteligente.\n\nEstou aqui para te auxiliar na jornada de uma vida mais saudável e feliz.\n\nHoje, vamos juntos verificar seu Índice de Massa Corporal (IMC) \n\n E te oferecer sugestões personalizadas de nutrição para alcançar seus objetivos.")

    def open_url(e):
        page.launch_url(e.data)

    github = ft.Markdown("## Se gostou do meu projeto, deixe uma estrela no meu repositório no [GitHub(victorlfdev)](https://github.com/victorlfdev/)", 
                  extension_set=ft.MarkdownExtensionSet.GITHUB_WEB, 
                  on_tap_link=open_url,
                        )


    def button_clicked(e):
        t.value = f"Meu nome é '{tb1.value}', '{tb2.value}Kg', '{tb3.value}cm', '{dd1.value}', '{dd2.value}'."
        response = chat_session.send_message(t.value)
        print(response.text)
        resposta.value = response.text
        b.disabled = True
        page.update()

    t = ft.Text()
    tb1 = ft.TextField(label="Digite seu nome", hint_text="Digite seu nome aqui")
    tb2 = ft.TextField(label="Digite seu peso", hint_text="Digite seu peso aqui")
    tb3 = ft.TextField(label="Digite sua altura", hint_text="Digite sua altura aqui")
    dd1 = ft.Dropdown(
            label="Faz atividade física?",
            hint_text="Faz atividade física?",
            options=[
                ft.dropdown.Option("Sim"),
                ft.dropdown.Option("Não"),
            ]
        )
    dd2 = ft.Dropdown(
            label="Qual seu objetivo estético?",
            hint_text="Qual seu objetivo estético?",
            options=[
                ft.dropdown.Option("Força"),
                ft.dropdown.Option("Definição"),
                ft.dropdown.Option("Hipertrofia"),
                ft.dropdown.Option("Emagrecimento"),
            ]
        )
    b = ft.ElevatedButton(text="Enviar", on_click=button_clicked)

    resposta = ft.Markdown(extension_set=ft.MarkdownExtensionSet.GITHUB_WEB)
    print(resposta.value)

    page.add(sobre, github,img, tb1, tb2, tb3, dd1, dd2, b, resposta)
    page.update()

ft.app(main)

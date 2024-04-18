import flet as ft

def main(page:ft.page):
  page.title="cadastro App"
 
  def cadastrar(e):
    print(preco.valeu)
   
  txt_titulo= ft.Text("titulo do produto:") #é oque vai ser escrito
 
  produto = ft.TextField(label="digite o titulo do produto", text_align=ft.TextAlign.LEFT) #é o input para o usuario
 
  txt_preço= ft.Text("preco do produto")
  preco= ft.TextField(value="0", label="digite o preço do produto", text_align= ft.TextAlign.LEFT)
 
  btn_produto= ft.ElevatedButton("cadastrar", on_click=cadastrar)#cria um botao

 
  page.add( # é onde as variaveis criadas tem que ser adicionadas para aparecer na pagina
    txt_titulo,
    produto,
    txt_preço,
    preco,
    btn_produto
     
    )
ft.app(target=main)# necessario no final do ocdigo
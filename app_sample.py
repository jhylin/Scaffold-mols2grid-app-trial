# Trial drawing molecules using RDKit only
# HTML and UI output

from shiny import ui, render, App

# from rdkit import Chem
# from rdkit.Chem.Draw import IPythonConsole
# from rdkit.Chem import Draw
# IPythonConsole.ipython_useSVG=True

# mol = Chem.MolFromSmiles("C1CC2=C3C(=CC=C2)C(=CN3C1)[C@H]4[C@@H](C(=O)NC4=O)C5=CNC6=CC=CC=C65")
# mol

app_ui = ui.page_fluid(
    ui.input_text("message", "Message", value="C1CC2=C3C(=CC=C2)C(=CN3C1)[C@H]4[C@@H](C(=O)NC4=O)C5=CNC6=CC=CC=C65"),
    #ui.input_checkbox_group("styles", "Styles", choices=["Bold", "Italic"]),
    # The class_ argument is used to enlarge and center the text
    ui.output_ui("some_html", class_="display-3 text-center")
)

def server(input, output, session):
    @output
    @render.ui
    def some_html():
        # x = input.message()
        # if "Bold" in input.styles():
        #     x = ui.strong(x)
        # if "Italic" in input.styles():
        #     x = ui.em(x)
        # return x

app = App(app_ui, server)
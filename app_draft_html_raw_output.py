# ---Test-in-progress, incomplete version---
# This trial app tries to use the to_pages() method in mols2grid
# to try to generate a HTML document in "pages" format 
# Unfortunately only the raw html document was shown in the app, 
#rather than the html webpage!


# ***Import all libraries or packages needed***
# Import shiny ui, app
from shiny import *
# Import shinywidgets
#from shinywidgets import output_widget, render_widget
# Import shinyswatch to add themes
import shinyswatch

# Import pandas
import pandas as pd

#import ipywidgets as ipy
#from IPython.display import HTML, IFrame, display

# Add RDKit, mols2grid
from rdkit import Chem
from rdkit.Chem import Draw
from io import StringIO
import mols2grid


# ***Specify data source***
# **Update data section**
# Example SMILES
# Canonical SMILES of calcitriol - CC(CCCC(C)(C)O)C1CCC2C1(CCCC2=CC=C3CC(CC(C3=C)O)O)C
# Canonical SMILES of ubiquinol - CC1=C(C(=C(C(=C1O)OC)OC)O)CC=C(C)CCC=C(C)CCC=C(C)CCC=C(C)CCC=C(C)CCC=C(C)CCC=C(C)CCC=C(C)CCC=C(C)CCC=C(C)C
# Canonical SMILES of glutamine - C(CC(=O)N)C(C(=O)O)N

smiles = """CC(CCCC(C)(C)O)C1CCC2C1(CCCC2=CC=C3CC(CC(C3=C)O)O)C, 
            CC1=C(C(=C(C(=C1O)OC)OC)O)CC=C(C)CCC=C(C)CCC=C(C)CCC=C(C)CCC=C(C)CCC=C(C)CCC=C(C)CCC=C(C)CCC=C(C)CCC=C(C)C,
            C(CC(=O)N)C(C(=O)O)N
"""
sm = StringIO(smiles)
df = pd.read_csv(sm, names = ["SMILES", "Names"])
df["mol"] = df.SMILES.apply(Chem.MolFromSmiles)


# User interface---
# Add inputs & outputs
app_ui = ui.page_fluid(
        # Add theme
        shinyswatch.theme.superhero(),
        # Add heading
        ui.h3("Headings"),
        # Input
        ui.row(
            # Specify input - ?allow different dataframes of SMILES for selection
            # ui.input_select(
            #     "SMILES",
            #     "Choose a compound:", 
            #     {"CC(CCCC(C)(C)O)C1CCC2C1(CCCC2=CC=C3CC(CC(C3=C)O)O)C": "calcitriol", 
            #      "CC1=C(C(=C(C(=C1O)OC)OC)O)CC=C(C)CCC=C(C)CCC=C(C)CCC=C(C)CCC=C(C)CCC=C(C)CCC=C(C)CCC=C(C)CCC=C(C)CCC=C(C)C": "ubiquinol"},
            # ),
            ui.input_action_button("go", "Go!", class_="btn-success"),
            ),
        # Output
        ui.output_ui("image")
        #output_widget("image")
    )


# Server---
# Add code within function 
def server(input, output, session):
    @output
    @render.ui
    @reactive.event(input.go, ignore_none=False)

    def image():
        
        img = mols2grid.MolGrid(df)
        a = img.to_pages()
        return a
  
    return image
    
        
# Combine UI & server into Shiny app
app = App(app_ui, server)
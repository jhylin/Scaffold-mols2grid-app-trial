# ---Test-in-progress, incomplete version---
# This is a convoluted way where a few example SMILES are saved into a dataframe,
# which is then fed into the app via using an action button (i.e. press button to action/input).
# The output is set up via mols2grid.save() to generate a stand-alone HTML document,
# which is saved in the working directory (open HTML webpage to see 2D molecular structures)


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

smiles = """CC(CCCC(C)(C)O)C1CCC2C1(CCCC2=CC=C3CC(CC(C3=C)O)O)C, calcitriol 
            CC1=C(C(=C(C(=C1O)OC)OC)O)CC=C(C)CCC=C(C)CCC=C(C)CCC=C(C)CCC=C(C)CCC=C(C)CCC=C(C)CCC=C(C)CCC=C(C)CCC=C(C)C, ubiquinol
            C(CC(=O)N)C(C(=O)O)N, glutamine
"""
sm = StringIO(smiles)
df = pd.read_csv(sm, names = ["SMILES", "Names"])
#df["mol"] = df.SMILES.apply(Chem.MolFromSmiles)


# User interface---
# Add inputs & outputs
app_ui = ui.page_fluid(
        # Add theme
        shinyswatch.theme.superhero(),
        # Add heading
        ui.h3("Headings"),
        # Place selection boxes & texts in same row
        ui.row(
            # Specify input
            ui.input_action_button("go", "Go!", class_="btn-success"),
            ),
        # Output
        ui.output_ui("image")
    )


# Server---
# Add code within the server function
def server(input, output, session):
    @output
    @render.ui
    @reactive.event(input.go, ignore_none=False)
    
    def image():

        mols2grid.save(df, output = "df-grid.html")

    return image

        
# Combine UI & server into Shiny app
app = App(app_ui, server)
**Latest update 9/8/2023**:

A new web app has been built with the similar concept as stated previously - code repository here: https://github.com/jhylin/Molviz_app

---

Old project summary from 12/7/2023:

Latest brainstorming idea was to change this project from purely on molecular scaffolds to using Datamol's visualisation function, Lasso highlighting (if this part works, then the CircleGrid function may be added in the future).

This hopefully will bring together RDKit, Datamol and Shiny in Python to build a molecular visualisation application to highlight molecular substructures from data inputs such as SMILES or SMARTS strings.

This project is currently a work-in-progress only.

---

Old project summary prior to 12/7/2023:

*Based on the idea of using mols2grid library and RDKit mainly***

This project is currently pending further progress from shinywidgets team regarding mols2grid package initialisation (or other solutions) as an [issue](https://github.com/rstudio/py-shinywidgets/issues/55) has been raised in their repository. Further work is likely only possible if there are changes to the issue raised at this point.

Three versions have been trialled which were showing either a standalone html document saved on working directory, raw html code showing in shiny app running in VS Code or another version using shinyswidget which only produced an output in terminal as "MolGridWidget()" with nothing displayed in the app yet. All of these versions were saved separately as individual Python scripts (except app_sample.py which was just a practise or sample version). None of them were the intended final version that I've hoped to reach at this stage.

An earlier Shiny app built using Python could be accessed [here](https://github.com/jhylin/Python_shiny_app/blob/main/app.py) if interested.

# Interactive security training platform based on CTF concept

This is my B.Sc. thesis, based on the [official AEI template](https://github.com/ksiminski/polsl-aei-theses) (with modifications). I hope it'll be useful to engineering students from the AEI faculty of the Silesian University of Technology who want to find some examples.

## Compiling the thesis (for POLSL students who are writing their own theses)

There are two versions of the thesis:

1. *Original* which can be compiled with `pdflatex` and `xelatex` (XeLaTeX uses Calibri on the title page)
2. *lualatex* on the [`lualatex` branch](https://github.com/krzysdz/inz-doc/tree/lualatex) which can be compiled with `lualatex` too and like the `xelatex` version uses Calibri. Templates for this version can be found in [my fork](https://github.com/krzysdz/polsl-aei-theses/tree/lualatex)

The compilation is fastest when using `pdflatex`, but if you want a nice title page use `xelatex` or `lualatex` and make sure that Calibri is installed.

### Requirements

- `pdflatex`, `xelatex` or `lualatex` depending on which one you want to use
- [Inkscape](https://inkscape.org/) (must be in the PATH) for SVG support
- [Python 3](https://www.python.org/) and [Pygments](https://pygments.org/) (`pip install Pygments`) for syntax highlighting
- JRE and [PlantUML](https://plantuml.com/) if you want to render UML diagrams
- Following TeX packages (some aren't really necessary):
  - `inputenc`, `fontenc`, `amsmath`, `amsfonts`, `amssymb`, `amsthm`, `babel`, `indentfirst`, `iftex`, `geometry`, `graphicx`, `hyperref`, `booktabs`, `tikz`, `pgfplots`, `mathtools`, `subcaption`, `appendix`, `csquotes`, `biblatex`, `ifmtarg`, `setspace`, `color`, `minted`, `ifplatform`
  - (XeTeX and LuaTeX) `fontspec`
  - (XeTeX) `xunicode`, `xltxtra`
  - (pdfTeX) `lmodern`

If you are using MiKTeX (probably the easiest way on Windows) it will ask you to install the required packages during first compilation.

### Rendering UML diagrams (optional)

The repository contains already rendered UML diagrams in SVG format, but if a change is made to the `.puml` sources, the diagrams must be rendered again.\
The command below should be enough, but if you want to know more, read the [documentation](https://plantuml.com/command-line)

```shell
java -jar /path/to/plantuml.jar -tsvg -o "/full/path/to/repo/uml/render" "/full/path/to/repo/uml/source"
```

If you are using only LuaTeX you can try the [plantuml](https://github.com/koppor/plantuml) [package](https://ctan.org/tex-archive/macros/luatex/latex/plantuml).

### Compiling

If you just want to compile the thesis using `pdflatex` on Windows or Linux, you can use the simple script `./build.ps1` which should work on any system with Bash or PowerShell.

#### Automatically in VS Code

The repository contains configuration for the [LaTeX Workshop (`James-Yu.latex-workshop`)](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop) plugin, which will automatically compile the PDF using `pdflatex` on source changes. On the `lualatex` branch there is a recipe using LuaLaTex, but it has to be selected manually.

#### Manually

Regardless of the engine, the process follows these steps:

1. `engine -shell-escape main`
2. `bibtex main`
3. `engine -shell-escape main`
4. `engine -shell-escape main`

Replace `engine` with `pdflatex`, `xelatex` or `lualatex` and that's all. `-shell-escape` is required, because the `minted` package must run shell commands to use Pygments. All 4 commands must be executed, [because TeX](https://tex.stackexchange.com/questions/342464/using-bibtex-and-pdflatex-why-are-three-latex-runs-needed).

You can also try using `latexmk`, but that will require Perl and reading some documentation to set `-shell-escape`.

#### Makefile

If you want to use it, you probably know how. I haven't used it in the project and can't guarantee that it'll work.

## The thesis and project (for those interested about the content)

The source code of the project is available in the [krzysdz/inz](https://github.com/krzysdz/inz) repository, which also contains a link to the platform with a some content. The link may work only occasionally as it was used mostly for testing.

The thesis in PDF format is available as [`main.pdf`](./main.pdf) and in [Releases](https://github.com/krzysdz/inz-doc/releases).

### Title

> Interactive security training platform based on CTF concept

### Abstract

> The popularity of the internet and its broad usage in the contemporary world introduces new problems in the form of vulnerabilities. One of the best ways to prevent them is good and practical cybersecurity education of developers responsible for the said web services. The thesis aims to design and create an easy-to-use platform suitable for education about web security using capture the flag challenges. The project combines this popular type of tasks with multiple-choice quizzes and allows rich descriptions of vulnerability types. The solution uses Docker and nginx proxy for easy automated challenge management.

### Keywords

> educational platform, cybersecurity training, CTF, web security, Docker

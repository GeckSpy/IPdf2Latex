# IPdf2Latex

**IPdf2LaTex** is a student project. The objective is to design a in-depght pedagogical ressources to make everyone with Python knowledge learn own to produce their own AI models converting images to their latex code equivalent. We have created a website (https://tutorial-ia-pe.readthedocs.io/) containing notebooks with all the knowledges you need and this GitHub repository containing the notebooks and the used ressources. The notebooks contains in-depht explanations, codes samples, exemples, exercies and codes.


# Existing project

Converting a entire Pdf or a simple mathematical formula to its equivalent LaTex code is a famous hard problem and even the best existing project are not perfect. Here is a non exaustive list of the best exiting project.
 - Mathpix (https://mathpix.com/pdf-to-latex): Best existing tool but not open source.
 - Nougat (https://github.com/facebookresearch/nougat): Try to convert full Pdf.
 - Pix2Tex (https://github.com/lukas-blecher/LaTeX-OCR): Focused on one ligne mathematical formula.
 - img2latex (https://github.com/kingyiusuen/image-to-latex)


# Datasets

The first part of a project of making such a model is to use a complete dataset by loading an existing one or creating your own and then manipulate it. For that we have created 4 notebooks to make you learn everything you need to know about datasets:
 - `Basics` teach you the very basic stuff about dealing with basic datasets.
 - `Images` teach you how to deal with images in Python and provide you usefull function for your future projects.
 - `Loading` teach you how to load an existing database from huggingface or with `sklearn`.
 - `Building` teach you how you can build your own dataset compose of images and text.

Then you will be able to have access to a large quantity of images like
<p style="text-align:center;">
    <img src="assets/formula1.png" />
</p>

associated with there equivalent Latex code
<p style="text-align:center;">
\begin{align*} L_{\vec{X}} \phi (\vec{X}) = \mbox{Tr}[J] \phi (\vec{X}) + P (\vec{V} \cdot \vec{\gamma})\end{align*}
</p>


# Model

There are various model that you can deside to use to make you AI model, but we have decided to finetune an Encoder/Decoder model.
<p style="text-align:center;">
    <img src="assets/model.png" />
    (Image took from im2latex project)
</p>

# Information

Do not hesitate to contect us nor o contribute to our project - see CONTRIBUTING.md

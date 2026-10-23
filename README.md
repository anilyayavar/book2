# Applied Audit Analytics with R

*Whole audit areas, from data to findings*, by [Anil Goyal](https://www.linkedin.com/in/anil-kumar-goyal/).

**Read the book online, free, at <https://anilyayavar.github.io/book2/>**

<a href="https://anilyayavar.github.io/book2/index.html"><img src="images/cover.jpg" alt="Cover of Applied Audit Analytics with R" width="300"/></a>

## About the book

A companion to [*R for Audit Analytics*](https://anilyayavar.github.io/new-book/). That book teaches the techniques one by one. This book applies them to whole audit areas, each worked from the data to the findings. The examples are Indian, and the data is simulated, with irregularities planted for the analysis to find.

1. **Accounts**. Journal entry testing, and reconciliation of records that should agree.
2. **Procurement and Payments**. Red flags in tendering, screens and models for bid rigging, and payables from the vendor master to the payment.
3. **Pay and Revenue**. Payroll and pensions, and revenue and tax.
4. **Schemes and Services**. Delays and pendency in public services, and a health insurance scheme audited from start to end.

An **Audit Question Finder** in the appendices lists common audit questions and the section that answers each one.

## Building the book

The book is written in [Quarto](https://quarto.org). To build it yourself, you need R (version 4.5 or later), Quarto (which comes with RStudio), and the R packages listed in the appendix *R Packages Used in This Book*. Then, in the project folder, run

```
quarto render
```

The rendered book is written to the `docs` folder, which GitHub Pages publishes.

## Licence, disclaimer and feedback

<a href="https://anilyayavar.github.io/book2/">Applied Audit Analytics with R</a> by Anil Goyal is licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). You may share and adapt it for non-commercial purposes, with credit to the author.

The author works for the Government of India. The opinions expressed in the book are personal to the author, and are not to be construed as those of the Government of India. All data in the book is simulated by the author. None of it pertains to any entity handled by the author in his official capacity.

Suggestions and corrections are welcome, by [email](mailto:anilyayavar@gmail.com) or through the [issues](https://github.com/anilyayavar/book2/issues) of this repository.

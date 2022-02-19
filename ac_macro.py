source = open('acronyms.tex', 'r')
out = open('generated_tex/acronym_macros.tex', 'w')

for line in source:
    s = line.split('{')[1][:-1]
    out.write(''.join([
        "\\newcommand{\\",
        s,
        "}{\\gls{",
        s,
        "} }\n"
    ]))

out.close()

import subprocess

ingredients = [
    ('R','Y','G'),
    ('R','Y','B'),
    ('R','Y','P'),
    ('R','G','B'),
    ('R','G','P'),
    ('R','B','P'),
    ('Y','G','B'),
    ('Y','G','P'),
    ('Y','B','P'),
    ('G','B','P'),

    ('R','Y','Y'),
    ('R','G','G'),
    ('R','B','B'),
    ('R','P','P'),
    ('Y','G','G'),
    ('Y','B','B'),
    ('Y','P','P'),
    ('G','B','B'),
    ('G','P','P'),
    ('B','P','P'),

    ('Y','R','R'),
    ('G','R','R'),
    ('B','R','R'),
    ('P','R','R'),
    ('G','Y','Y'),
    ('B','Y','Y'),
    ('P','Y','Y'),
    ('B','G','G'),
    ('P','G','G'),
    ('P','B','B'),

    ('R','R','R'),
    ('Y','Y','Y'),
    ('G','G','G'),
    ('B','B','B'),
    ('P','P','P'),
]

subprocess.run(['lualatex', '--jobname=recipe_card_back', '--output-directory=Images/TTSCards', './recipe_card_back.tex'])
subprocess.run(['convert', 'Images/TTSCards/recipe_card_back.pdf', 'Images/TTSCards/recipe_card_back.png'])

for x,y,z in ingredients:
    argstring = r'\newcommand\first{%s}\newcommand\second{%s}\newcommand\third{%s}'% (x,y,z)
    # print(argstring)

    command_string = '"' + argstring + r'\input{./recipe_card.tex}' + r'"'

    print(command_string)

    subprocess.run(['lualatex', '--jobname=recipe_card_%s%s%s' % (x,y,z), '--output-directory=Images/TTSCards', command_string])
    subprocess.run(['convert', 'Images/TTSCards/recipe_card_%s%s%s.pdf' % (x,y,z), 'Images/TTSCards/recipe_card_%s%s%s.png' % (x,y,z)])

subprocess.run('rm ./Images/TTSCards/*.log', shell=True)
subprocess.run('rm ./Images/TTSCards/*.aux', shell=True)
subprocess.run('rm ./Images/TTSCards/*.pdf', shell=True)
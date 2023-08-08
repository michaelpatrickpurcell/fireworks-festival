import subprocess

ingredients = [('Y','Y','Y')]
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
# Selecionando professores e número de horas:
query = '''SELECT P.nomeprof, H.numhoras
FROM PROFESSOR as P, HORARIO as H, PROFTURMA as PT
WHERE P.codprof=PT.codprof AND PT.anosem=H.anosem'''

# Listando salas com horários livres e ocupados:
# Essa aqui eu não entendi bem como fazer
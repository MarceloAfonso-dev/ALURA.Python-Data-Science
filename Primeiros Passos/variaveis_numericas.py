q_seguranca = 5
s_seguranca = 3000

q_docente = 16
s_docente = 6000

q_diretoria = 1
s_diretoria = 12500

total_empregados = q_seguranca + q_docente + q_diretoria

diferenca_salario = s_diretoria - s_seguranca

media = (q_seguranca*s_seguranca + q_docente*s_docente + q_diretoria*s_diretoria)/total_empregados

print(total_empregados, diferenca_salario, media)
class CPF:
  def __init__(self, cpf):
    self.cpf = ''.join(filter(str.isdigit, cpf))

  def validar(self):
    if len(self.cpf) != 11:
        return False


    soma = 0
    for i in range(9):
       soma += int (self.cpf[i]) * (10-i)
    resto = soma % 11
    if resto < 2:
       digito_1 = 0
    else:
       digito_1 = 11 - resto

    if int(self.cpf[9]) != digito_1:
            return False

    soma = 0

    for i in range (10):
       soma += int(self.cpf[i]) * (11 - i)
       resto = soma % 11
    if resto < 2:
       digito_2 = 0
    else:
       digito_2 = 11 - resto

    if int(self.cpf[10]) != digito_2:
            return False

    return True


cpf = CPF("07820827781")

if cpf.validar():
    print("CPF válido")
else:
    print("CPF inválido")
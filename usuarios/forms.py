from django import forms


class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label="Nome de Login",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Ex.: Thaís Moreira"}
        ),
    )
    senha = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        # passando attributes para o formulario para estilização
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Digite a sua senha"}
        ),
    )


class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label="Nome de cadastro",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Ex.: Thaís Moreira"}
        ),
    )
    email = forms.EmailField(
        label="Email",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: thais_moreira@xpto.com",
            }
        ),
    )
    senha_1 = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        # passando attributes para o formulario para estilização
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Digite a sua senha"}
        ),
    )

    senha_2 = forms.CharField(
        label="Confirme sua senha",
        required=True,
        max_length=70,
        # passando attributes para o formulario para estilização
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite a sua senha novamente",
            }
        ),
    )

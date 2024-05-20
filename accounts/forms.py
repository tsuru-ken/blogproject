
# UserCrationFormのインポート
from django.contrib.auth.forms import UserCreationForm

# models.pyで定義したカスタムUserモデルをインポート
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        
        models = CustomUser
        fields = ('username','email','password1','password2')
        

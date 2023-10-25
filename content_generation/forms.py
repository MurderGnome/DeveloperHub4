
from .models import LearningOutcome

class LearningOutcomeForm(forms.ModelForm):
    class Meta:
        model = LearningOutcome
        fields = ['title', 'description', 'STS_line_item']

from .models import Assessment

class AssessmentForm(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = ['question_type', 'question_text', 'answer']

from .models import Rubric

class RubricForm(forms.ModelForm):
    class Meta:
        model = Rubric
        fields = ['criteria', 'level_of_mastery', 'points']

from .models import LearningActivity

class LearningActivityForm(forms.ModelForm):
    class Meta:
        model = LearningActivity
        fields = ['activity_type', 'description']

class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['name', 'description']

class STSLineItemForm(forms.ModelForm):
    class Meta:
        model = STSLineItem
        fields = ['name', 'description']

class LearningOutcomeForm(forms.ModelForm):
    class Meta:
        model = LearningOutcome
        fields = ['name', 'content']

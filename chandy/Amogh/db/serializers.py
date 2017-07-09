from rest_framework import serializers
from models import CreateUser, Points, DoneTuts


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Points
        fields = ('')

class DoneTutsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoneTuts
        fields = ('One_At_A_Time','Jumbler_Excercise','Full_Excercise','Excel_Data_Entry','Selection_of_cells','Simple_Data_Entry_I','Simple_Data_Entry_II','Cell_Size_Excercise','Basic_Number_Data_Entry_Tricks','Extra','Current_Directory_file_upload','Current_Directory_file_upload_with_specific_extension',)

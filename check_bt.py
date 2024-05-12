# Online Python - IDE, Editor, Compiler, Interpreter
'''Check red blood cell compatibility between donor and recipient.

For simplicity, only eight basic types of blood are considered.

The input of blood type can be in the form of:

Bloodtype enumeration
An integer value between 0 and 7
Textual representation e.g. "0-", "B+", "AB+", ...'''

def check_bt(group, donor, recipient):
    o_donors = ['A−', 'A+', 'B−', 'B+', 'AB-', 'AB+', 'O+', 'O-']
    a_recipients = ['O−', 'O+', 'A−', 'A+']
    a_donors = ['A−', 'A+', 'B−', 'B+', 'AB-', 'AB+']
    b_donors = ['O-', 'O+', 'B-', 'B+']
    b_recipients = ['B−', 'B+', 'AB-', 'AB+']
    ab_recipients = ['A−', 'A+', 'B−', 'B+', 'O+', 'O-']
    rh_positive_recipients = ['Rh-', 'Rh+']
    
    if (group == 'O-'):
        if donor in o_donors:
            return True
        if recipient == 'O-':
            return True
        else:
            return False
    elif ((group == 'A-') or (group == 'A+')):
        if recipient in a_recipients:
            return True
        if donor in a_donors:
            return True
        else:
            return False
    elif ((group == 'B-') or (group == 'B+')):
        if donor in b_donors:
            return True
        if recipient in b_recipients:
            return True
        else:
            return False
    elif ((group == 'AB-') or (group == 'AB+')):
        if recipient in ab_recipients:
            return True
        if donor not in ab_recipients:
            return True
        else:
            return False
    elif (group == 'Rh-'):
        if (recipient == 'Rh-'):
            return True
        else:
            return False
    else:
        if recipient in rh_positive_recipients:
            return True
        else:
            return False

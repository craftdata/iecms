# coding: utf-8
# Copyright (C) Nyimbi Odero, 2017-2018
# License: MIT
import sys

imp_add = 0
code = []
imports = []
class_names = []
jt = []


# Write code to filename
def code_write(list_name, filename):
    thefile = open(filename, 'w')
    for item in list_name:
        thefile.write("%s\n" % item)
    thefile.close()
    
def camelCase(st):
    output = ''.join(x for x in st.title() if x.isalpha() or x == '_')
    #return output[0].lower() + output[1:]
    return output[0].upper() + output[1:]
    
def init_fixup(filename):

    global imp_add, imports, class_names, code, jt
    join_tables = []
    
    
    with open(filename, 'r') as f:
        code = f.read().splitlines()
        for i in range(len(code)):
            # General Fixups
            code[i] = code[i].replace("nullable=False", "nullable=True",1)
            code[i] = code[i].replace("INTERVAL(fields='day to second')","Interval",1)
            code[i] = code[i].replace("BLOB","LargeBinary",1)
            
            if code[i].startswith('import') or code[i].startswith('from '):
                imports.append(i)
            if code[i].startswith('class '):
                code[i] = code[i].replace('(Base)', '(Model)',1)
                # Get the classname
                (a, _, _)  = code[i].partition('(')
                b = a.split()
                class_names.append(b[1])
                #code.insert(i+2, photo_hdr)
            
            ## Join Tables
            if code[i].startswith('t_'):
                # http://docs.sqlalchemy.org/en/latest/orm/extensions/declarative/table_config.html
                # Using a hybrid approach
                #class MyClass(Base):
                #   __table__ = Table(
                cd = code[i]
                
                # t_some_thing = Table(
                (l,c,r) = cd.partition('=')
                s ='class '+ camelCase(l)+'(Model):\n\t __table__ = ' + r
                # In case the name is repeated
                if s not in join_tables:
                    join_tables.append(s)
                    jt.append(camelCase(l))
                else:
                    s = 'class ' + camelCase(l) + '_2(Model):\n\t __table__ = ' + r
                    join_tables.append(s)
                    t = camelCase(l)
                    t += '_2'
                    jt.append(t)
                code[i] = s
                #pass
            
        class_count = len(class_names)
        # Debug stuff
        print(class_count)

def add_imports(impt):
    global imp_add, imports, class_names, code
    
    imp_add += 1
    code.insert(imp_add, impt+ '\n')
    
# Takes two strings
def add_mixin(class_name, mix_in):
    global imp_add, imports, classes, code
    
    # find the ( and replace with ( Mixin,
    for i in range(len(code)):
        if code[i].startswith('class '):
            (a, _, _) = code[i].partition('(')
            b = a.split()
            if b[1] == class_name:
                code[i] = code[i].replace('(', '( ' + mix_in + ', ')
    




# Returns the line number on which the class declaration is made
def find_class(class_name):
    global code
    for i in range(len(code)):
        if code[i].startswith('class '):
            (a, _, _) = code[i].partition('(')
            b = a.split()
            if b[1] == class_name:
                return i
    return 0
    
# Given line number, finds the next class
def find_next_class(line):
    global code
    for i in range(line, len(code)):
        if code[i].startswith('class '):
            return i
    return 0
    
    
    
    
# We add new code to the top
def add_field_top(class_name, field_code):
    global imp_add, imports, class_names, code
    i = find_class(class_name)
    if i > 0:
        code[i + 2].insert(field_code)


def add_field_below(class_name, field_code):
    global imp_add, imports, class_names, code
    i = find_next_class( find_class(class_name) )
    if i > 0:
        code[i - 2].insert(field_code)



if __name__ == '__main__':
    # Initialize Variables
    fname = sys.argv[1]
    init_fixup(fname)
    
    print("fixup_models:   ...Finished Init Fixup ...")
    code_write(class_names, 'class_names.txt')
    code_write(jt, 'join_tables.txt')
    
    # Add AuditMixin Across the board
    for x in class_names:
        add_mixin(x,'AuditMixin')
    
    
    # it it has the name 'type' or category' add RefTypeMixin
    for x in class_names:
        if x.endswith('type') or \
                x.endswith('category') or\
                x.endswith('rank') or \
                x.endswith('station') or \
                x.endswith('class') or\
                x.endswith('role') or\
                x.endswith('list') or\
                x.endswith('team'):
            
            add_mixin(x, 'RefTypeMixin')

    for x in class_names:
        if x.endswith('officer'):
            add_mixin(x, 'PersonMixin')
            
    # Adding all the mixin's
    
    # PersonDocMixin
    add_mixin('Nextofkin', 'PersonMixin, PersonDocMixin, ContactMixin')
    add_mixin('Biodata',   'PersonDocMixin, PersonMedicalMixin, BiometricMixin, ParentageMixin')
    
    # DocMixin
    add_mixin('Document',  'DocMixin')
    add_mixin('Transcript', 'DocMixin')
    add_mixin('Exhibit',  'DocMixin')
    
    # RefTpeMixin
    add_mixin('Lawfirm',   'RefTypeMixin, ContactMixin')
    add_mixin('Discipline','RefTypeMixin')
    add_mixin('Csiequipment','RefTypeMixin')
    
    # PersonMixin
    add_mixin('Party','PersonMixin, ContactMixin')
    add_mixin('Lawyer','PersonMixin, ContactMixin')
    add_mixin('Prosecutor','PersonMixin, ContactMixin')
    
    # ActivityMixin
    add_mixin('Courtcase','ActivityMixin')
    add_mixin('Hearing','ActivityMixin')
    add_mixin('Commital','ActivityMixin')
    add_mixin('Healthevent','ActivityMixin')
    add_mixin('Investigationdiary','ActivityMixin')
    
    # PlaceMixin
    add_mixin('Court', 'PlaceMixin')
    add_mixin('Prison', 'PlaceMixin')
    add_mixin('Lawfirm', 'PlaceMixin')
    add_mixin('Policestation', 'PlaceMixin')
    add_mixin('Sysuserextra', 'ContactMixin')
    
    add_mixin('County', 'RefTypeMixin')
    add_mixin('Subcounty', 'RefTypeMixin')
    add_mixin('Ward', 'RefTypeMixin, PlaceMixin')
    add_mixin('Town', 'RefTypeMixin, PlaceMixin')
    
    
    

    
    #add_imports(std_hdr)
            
    code_write(code, 'models.py')
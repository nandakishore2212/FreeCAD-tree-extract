#Python code to be run from FreeCAD Daily (Verson 0.17 : 18/05/17)
#using command $execfile('/home/nandakishore/Documents/finalfreecode.py')
#or other location as accordingly

#Function to traverse the Assembly hierrchy tree structure and print the output into output.xml

def findchildren(ob, reqflag, obparent, level, required):

    if len(ob.OutList) > 0:                      #Check if the current object has children objects
        flag = 0
        for child in ob.OutList:
            for word in unwanted:
                if word in str(child.Label):
                    flag = 1
        if ob.Label in required:
            opfile.write("<li>")
            opfile.write("<id>assembly</id>")
            opfile.write("<assembly>")
            opfile.write(ob.Label)
            opfile.write("</assembly>")
            reqflag = 1
            for parent in ob.InList:
                obparent = parent
        if level <= 3:
            if flag == 0:
                if reqflag ==1:
                    opfile.write("<ul>")                     #Every new generation of objects should be under individual <ul>
                    level = level + 1
                for child in ob.OutList:
                    if reqflag == 1:
                        opfile.write("<li>")                 #Every object should be under individual <li>. Children are nested inside parent <ul> and <li> accordingly
                        opfile.write("<id>component</id>")
                        opfile.write("<component>")
                        opfile.write(child.Label)            #Write the object Label to the output file
                        opfile.write("</component>")
                        findchildren(child, reqflag, obparent, level)                  #Repeat loop execution till a generation of objects is reached without children
                        opfile.write("</li>")
                    else:
                        findchildren(child,reqflag, obparent, level)
                if reqflag == 1:
                    opfile.write("</ul>")
                    level = level - 1

    if (ob in obparent.OutList) and (reqflag ==1):
        reqflag = 0
        opfile.write("</li>")




#import '/home/nandakishore/Documents/KonzeptB_lang090715.stp'
dc = App.ActiveDocument                          #Holds a reference to the current document. It is assumed the STP file is already imported
                                                 #Else, an import command should be used first to import the file
#obj = dc.KonzeptB_lang_stp                       #Root parent object, usually the name of the imported STP file

unwanted =  ['X_Axis', 'Y_Axis','Z_Axis','XY_Plane','XZ_Plane', 'YZ_Plane','SOLID', 'COMPOUND'] #If the object name contains any of these, ignore it

opfile = open("/home/nandakishore/Documents/output_label_4level.xml", "w")   #Output is stored inside output.xml
opfile.write("<ul>\n")
opfile.write("<li>")
opfile.write("<id>system</id>")
opfile.write("<system>")
#opfile.write(obj.Label)
opfile.write("KonzeptB_lang_stp")
opfile.write("</system>")
#level1 = 1
#findchildren(obj,level1)                                #Function is called to traverse the tree structure and print output to file

required2 = ['Steuergerte_CellCelector', 'Inkubator_Liconic_mit_Transfer_oa3366', 'Racktraeger',
    '__Lage_Pipetten_Rundmagazin_oa3063', '__Lage_Pipetten_Rundmagazin_oa462', 'Tubemagazingesamt',
            'Part__Feature2471', 'Part__Feature1836']

#ImportGui.insert(u"/home/nandakishore/Documents/729-00-00-000_StemCellFactory_19_11_14_stp.stp","Unnamed")
dc = App.ActiveDocument                          #Holds a reference to the current document. It is assumed the STP file is already imported
                                                 #Else, an import command should be used first to import the file
obj = dc._29_00_00_000_StemCellFactory_26_02_13_stp
level2 = 1
obparent = obj
opfile.write("<ul>")                     #Every new generation of objects should be under individual <ul>
findchildren2(obj,0, obparent,level2)
opfile.write("</ul>\n")

opfile.write("</li>\n")
opfile.write("</ul>\n")
opfile.close()

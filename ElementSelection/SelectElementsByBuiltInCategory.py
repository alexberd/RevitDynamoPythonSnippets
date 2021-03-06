# Enable Python support and load DesignScript library
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# Import DocumentManager and TransactionManager
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

# Import RevitAPI
clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

#Select Current Document
doc = DocumentManager.Instance.CurrentDBDocument

#Create ElementCollector
selection = FilteredElementCollector(doc);

#Select Built-in Cateogry based on the follow link
#https://www.revitapidocs.com/2016/ba1c5b30-242f-5fdc-8ea9-ec3b61e6e722.htm
selection.OfCategory(BuiltInCategory.OST_Views)
#selection.OfClass(View);

#Define if element is a type element or not
#selection.WhereElementIsNotElementType();

#Append the elements to output
output=[]
for i in selection:
	output.append(i)
OUT = output

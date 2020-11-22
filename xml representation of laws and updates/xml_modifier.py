import sys
import xml.etree.ElementTree as ET

class Xml_modifier:
    def __init__(self):
        original_law_xml=sys.argv[1]
        fix_law_xml=sys.argv[2]
        
        self.original_tree = ET.parse(original_law_xml)
        self.original_root = self.original_tree.getroot()
        
        self.fix_tree = ET.parse(fix_law_xml)
        self.fix_root = self.fix_tree.getroot()

    def change(self,element,id,full_content,date):
        """
        :param element: The element type - paragraph or section.
        :param id: The secion id to be modified.
        :param full_content: The full text of the modified element.
        :param date: Date of fixing TODO- decide if date should stay as a paramete?
        :return: void
        """
        pass

    def delete(self,element,id):
        """
        :param element: The element type - paragraph or section.
        :param id: The element id to be deleted.
        :return: void
        """
        # self.original_law_xml=self.original_law_xml+" changed"
        pass

    def add(self,element,after_element_id ,full_content):
        """
        :param element: The element type - paragraph or section.
        :param after_element_id: The id of the element to be added after. 
        :param full_content:The full text of the added element.
        :return:
        """
        pass

    def main(self):
        next_element=""
        index=0
       
        # print(self.fix_root.tag)
        # print(self.original_root.tag)
        for description in self.original_root.iter('section'):
            print(description.text)

        for description in self.original_root.iter('section'):
            description.text="avishai"

        for description in self.original_root.iter('section'):
            print(description.text)

        self.original_tree.write("output.xml", encoding="UTF-8")



# https://towardsdatascience.com/processing-xml-in-python-elementtree-c8992941efd2
# python xml_modifier.py original_law.xml fix_law.xml

        # while(next_element != "</fix_form>")


        
if __name__ == "__main__":
    x=Xml_modifier()
    x.delete(1,2)
    x.main()

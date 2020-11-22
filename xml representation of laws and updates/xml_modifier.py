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

    def update(self,fix_element,output_element):
        """
        :param fix_element: the element to fix
        :param output_element: The element of the output with its origenal value
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


    def iterate_sections(self):
       
        # print(self.fix_root.tag)
        # print(self.original_root.tag)
        for element in self.original_root.iter('section'):
            text = element.text
            for sub_element in element.iter():
                if sub_element.tag == "note":
                    text = text + "<note>"+sub_element.text+"</note>"
                text= text + sub_element.tail
            print("\n section text: "+text.translate(str.maketrans('', '', '\n\r\t')))
        
        pass

    def iter_n_print(self,element):
        if element.tag != None:
            print("<"+element.tag+">"+element.text)
            for sub_element in element:
                self.iter_n_print(sub_element)

            print("</"+element.tag+">"+str(element.tail))

        pass


    def update_blank(self,element, output_element ):
        if element.get("action") == "remove":
            return None
        return None


    def get_output_element(self,element_type, output_content_id):
        _id = 0
        target_id = int(output_content_id)
        for content in self.original_root.iter(element_type):
            _id = _id +1 
            if _id == target_id:
                return content
        return None
    

    def main(self):
        for content in self.fix_root.iter('content'):
            output_content = self.get_output_element('content',content.get("id"))
            if content.get("action") == "update-blank":
                self.update_blank(content, output_content)
            
            elif content.get("action") == "update":
                self.update(content, output_content)
            
            elif content.get("action") == "add":
                self.add(content, self.original_root)
            
            elif content.get("action") == "remove":
                self.fix_root.remove(content)
    

        # for description in self.original_root.iter('section'):
        #     description.text="avishai"

        # for description in self.original_root.iter('section'):
        #     print(description.text)

        # self.original_tree.write("output.xml", encoding="UTF-8")



# https://towardsdatascience.com/processing-xml-in-python-elementtree-c8992941efd2
# python xml_modifier.py original_law.xml fix_law.xml

        # while(next_element != "</fix_form>")


        
if __name__ == "__main__":
    x=Xml_modifier()
    x.delete(1,2)
    x.main()

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

    def get_output_element(self,element, output_element):
        """
        :param element: the element to fix in the fix-form
        :param output_element: The element of the output which contain the 
        """
        _id = 0
        target_id = int(element.get("id"))
        for content in output_element.iter(element.tag):
            _id = _id +1 
            if _id == target_id:
                return content
        return None

    def update(self,fix_element,output_element):
        """
        :param fix_element: the element to fix
        :param output_element: The element of the output with its origenal value
        :return: void
        """
        pass

    def delete(self,sub_element,output_element):
        """
        :param element: The sub element from the fix-form
        :param id: the element from the law-form which need to remove the sub-element.
        :return: void
        """
        output_element.remove(self.get_output_element( sub_element,output_element))
        # self.original_law_xml=self.original_law_xml+" changed"
        pass

    def add(self,element,output_containing_element ):
        """
        :param element: The element type - paragraph or section.
        :param output_containing_element: The output element which need to contain the new element
        :return:
        """
        index = 0
        element_tag_index = 0 # the counter for the elements of the element.tag
        for output_sub_element in output_containing_element.iter():
            index = index +1
            if output_sub_element.tag == element.tag:
                element_tag_index = element_tag_index + 1
            if element_tag_index ==int(element.get("id")):
                output_containing_element.insert(index,element)
                return
        


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
        for sub_element in element.iter():
            if sub_element.tag != None:
                if sub_element.get("action") == "remove":
                    self.delete(sub_element,output_element)
                elif sub_element.get("action") == "update-blank":
                    self.update_blank(sub_element,self.get_output_element(sub_element,output_element))
                elif sub_element.get("action") == "update":
                    self.update(sub_element,self.get_output_element(sub_element,output_element))
                elif sub_element.get("action") == "add":
                    self.add(sub_element, output_element)


    
    

    def main(self):
        for content in self.fix_root.iter('content'):
            output_content = self.get_output_element(content,self.original_root)
            if content.get("action") == "update-blank":
                self.update_blank(content, output_content)
            
            elif content.get("action") == "update":
                self.update(content, output_content)
            
            elif content.get("action") == "add":
                self.add(content, self.original_root)
            
            elif content.get("action") == "remove":
                self.delete(content,self.fix_root)
    

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

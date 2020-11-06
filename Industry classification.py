
import os
import shutil

# Code description:
# Sort the files in the specified folder: move the files containing the keyword "futures" to the futures folder,
# and move the files containing the keywords "sugar and soybean meal" to the agricultural product folder
classify_lists = {

    'futures': ['agricultural product']
                }

classify_lists2 = {

    'agricultural product': ['sugar','soybean meal']

}

def classify_files(path):
    '''
    # input : the path of pending folder
    '''
    
    if not os.path.isdir(path):
        return

    # list all PDFs
    pdf_files = [name for name in os.listdir(path) if  name.endswith(".pdf")]

    for pdf_name in pdf_files:
        #Processing header time and broker name
        #pdf_names = pdf_name.split('-')
        #name = pdf_names[len(pdf_names) - 1]

        name = pdf_name

        for classify1 in classify_lists:
            
            # Create folders by level-1
            classify1_path = os.path.join(path,classify1)
            old_pdf_path = os.path.join(path,pdf_name)
            if not os.path.exists(classify1_path):
                os.makedirs(classify1_path)       
            for classify2 in classify_lists[classify1]:
                if classify2 in name:
                    # Create folders by level-2
                    classify2_file = os.path.join(classify1_path,classify2)
                    if not os.path.exists(classify2_file):
                        os.makedirs(classify2_file)                          
                    # processing PDF name
                    pdf_names = pdf_name.split('.')
                    #new_name = pdf_names[0] + "_" + classify1 + '_' + classify2 + '.pdf'
                    
                    new_name = pdf_names[0] + '.pdf'
                    new_pdf_path = os.path.join(classify2_file,new_name)
                    if not os.path.exists(new_pdf_path) and os.path.exists(old_pdf_path):
                        shutil.move(old_pdf_path,new_pdf_path)
                        print(pdf_name + ' Cut to[' + classify1 + '-' + classify2 + ']')
                    break
                if classify2 in classify_lists2.keys():
                    for classify3 in classify_lists2[classify2]:
                        if classify3 in name:
                            # Create folders by secondary classification
                            classify2_file = os.path.join(classify1_path,classify2)
                            if not os.path.exists(classify2_file):
                                os.makedirs(classify2_file)                          
                            # processing PDF name
                            pdf_names = pdf_name.split('.')
                            
                            #new_name = pdf_names[0] + "_" + classify1 + '_' + classify2 + '.pdf'
                            new_name = pdf_names[0] + '.pdf'
                            new_pdf_path = os.path.join(classify2_file,new_name)
                            if not os.path.exists(new_pdf_path) and os.path.exists(old_pdf_path):
                                shutil.move(old_pdf_path,new_pdf_path)
                                print(pdf_name + ' cut to [' + classify1 + '-' + classify2 + ']')
                            break

            if classify1 in name:
                pdf_names = pdf_name.split('.')
                new_name = pdf_names[0] + "_" + classify1  + '.pdf'
                new_pdf_path = os.path.join(classify1_path,new_name)
                if not os.path.exists(new_pdf_path) and os.path.exists(old_pdf_path):
                    shutil.move(old_pdf_path,new_pdf_path)
                    print(pdf_name + ' cut to [' + classify1 + '-' + classify2 + ']')
                break


if __name__=='__main__':
    classify_files(r'C:\Users\Administrator.SKY-20170217SWK\Desktop\test')





#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!pip install streamlit
#!pip3 install --upgrade tensorflow
#!pip3 install --upgrade keras


# In[3]:


import streamlit as st
import os
import asyncio
from PIL import Image

def get_or_create_eventloop():
    try:
        return asyncio.get_event_loop()
    except RuntimeError as ex:
        if "There is no current event loop in thread" in str(ex):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            return asyncio.get_event_loop()

def save_uploadedfile(uploadedfile):        
    filename=uploadedfile.name
    filename_new="tmp_image." + filename.split(".")[-1]    
    with open(os.path.join("./data/tmp/",filename_new),"wb") as f:
        f.write(uploadedfile.getbuffer())
        #st.success(\"Saved File:{} to ./data/tmp/\".format(uploadedfile.name)) 
    return filename_new                           
        
        
def load_image():
    col1, col2= st.columns(2) # divide the display in 2 cols
    #col1, col2= st.columns([10,10]) # divide the display in 2 cols
    st.sidebar.write("## Pick a painting :gear:")
    uploaded_file = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    #uploaded_file = st.file_uploader(label='Pick a painting to test')
    if uploaded_file is not None:
        image_data = uploaded_file.getvalue()        
        #st.image(image_data)
        name_file = uploaded_file.name 
        filename_new=save_uploadedfile(uploaded_file)
        
        import Paleta_picture
        df_colours=Paleta_picture.exact_color("./data/tmp/",filename_new, 500, 10, 2.5,500)
        df_colours.to_csv('./data/tmp/tmp_df_colours.csv',index=False)
        image_resize= Image.open('./data/tmp/tmp_resize_image.jpg')
        
        with col1:
            st.header("Original picture")
            st.image('./data/tmp/tmp_resize_image.jpg')
            st.write("___")
            
            st.write("## Palette")
            st.image('./data/tmp/tmp_palette_colours.png')
            

        #col1.image(image_resize, 'Original image')#, use_column_width=True
        #image_colors= Image.open('./data/tmp/tmp_palette_colours.png')
        #col1.image(image_colors, caption='Palette of colours') 
        
        #path_in = uploaded_file.name
        #print(path_in)
        #%run -m Paleta_picture
        
def main():
    
    #get_or_create_eventloop()
    st.set_page_config(layout="wide", page_title="Painting suggester")
    #st.title('Painting suggester')
    load_image()
    


if __name__ == '__main__':
    main()


# In[ ]:





# In[ ]:





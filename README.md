# DESU_DS
analyzing brain images to discover age marker

This codes analyze the braib MRI images and extract the important feauture in aging in the somatosensorimotrice pathways.
steps:
1. first we clusters the brain MRI images using MVPC method which is in MVPC-NEW.ipynb _ In this code we used Kmeans and Agglomerative Clustering method. Finally we used the results of kmeans because it  had a better cosistensy with the aging index. 
2. Then we extracted the RDM by the representational similarity method which is in the RSA.py file. 
3. The we analyzed the results of RDM in excel.
4. In the last step we used the Feature importance method to extract the importance of each feature. we read the excel file consists of all the data and also the MVPC and RSA results. The code are in the Feature_importance.ipynb file

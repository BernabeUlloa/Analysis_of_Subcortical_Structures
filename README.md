# Analysis_of_Subcortical_Structures
Structural magnetic resonance imaging (MRI) is an imaging technique that uses magnetic resonance to obtain detailed, high-resolution images of organs and internal structures of the body. Freesurfer[1] is a software for processing structural brain MRI images used to analyze brain anatomy and measure cortical volume and surface area. Freesurfer employs automatic segmentation techniques to identify different brain structures and extract quantitative measures. One of these measures is the calculation of the average intensity within a brain region, which can be useful in medical and scientific research for studying brain activity in different regions and comparing them. This measure can also be helpful in diagnosing neurological diseases such as Alzheimer's disease, which is characterized by a decrease in gray matter density in certain brain regions. Furthermore, calculating the average intensity within a brain region can be useful for surgical planning.

## Code Structure
We have subjects from the public HCP database[2], each with their T1 structural image (orig.nii.gz), corresponding subcortical segmentation (aseg.nii.gz), and labels for each structure.

For each subject, the aseg.nii.gz file was used to identify the voxels corresponding to each anatomical structure, generating a mask. Next, the mask was applied to extract the original intensity values from the subject's orig.nii.gz image.

![Alt text](/img/Figure_2.png)
Subsequently, the intensity level of the segmented regions was calculated for each subject. We calculated the average intensity values using arithmetic mean and standard deviation. Finally, we calculated the coefficient of variation for each region using the following formula:
$$CV = 100 * \frac{\sigma}{\mu}$$

## Result
Next, we can observe the results of applying the mask to a specific region of the brain for a specific slice, along with their original intensities.

![Alt text](/img/Figure_3.png)
From isolated regions using the one shown above, intensity calculations were performed and recorded in the following table.

|Region	|103818	|105923	|111312	|Arithmetic mean of average intensity	|σ Standard deviation of average intensity	|Variation Coefficient	|% Variation Coefficient|
| ---|--- |--- |--- |--- |--- |--- |--- |--- |
|20	|Right-Cerebral-White-Matter	|199,29 |	190,19	|199,29	|196,26	|5,25	|2,68|2,68|
|0	|Left-Cerebral-White-Matter	|198,91	|189,45	|198,91	|195,76|5,46	|2,79	|2,79|

Note that the table only displays information for a couple of regions and three subjects as an example.

## Conclusions
During the code creation process, the correct functionality was initially tested for a single subject, and then the remaining subjects were added. In this process, it was observed that there is a significant variation in coefficients that increases as the number of samples increases, reaching approximately 10% in most regions when all 10 subjects are included (see attached results.xlsx). This suggests that there is not only anatomical but also functional variability among the subjects, as the intensity values also vary according to their activation. It is possible that part of this variation is due to sampling and processing errors, but it still represents considerable figures.

## Reference
> [1] Surfer NMR MGH Harvard. https://surfer.nmr.mgh.harvard.edu. (accessed on 17 April 2023).
> [2] Human Connectome Project Young Adult Study. “1200 Subjects Data Release”. https://www.humanconnectome.org/study/hcp-young-adult/document/1200-subjects-data-release. (accessed on 17 April 2023).

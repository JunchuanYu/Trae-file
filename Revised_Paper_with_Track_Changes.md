# Revised Paper with Track Changes (Red Marked & Chinese Bilingual)

> [!NOTE]
> **修改说明 (Revision Note)**: 
> 1. 删减的内容使用 <del style="color:red;">红色删除线</del> (strikethrough) 标记，新增或修改的内容使用 <strong style="color:red;">红色加粗</strong> (bold) 标记。
> 2. 已根据要求将所有的“InSAR地表形变聚集区”等描述统一修改为 **InSAR deformation anomaly zones**，将“滑坡关联的”统一修改为 **Landslide-related**。
> 3. 在每个英文段落下方，使用引用块 `> [中文对照]` 附上了原 `docx` 中对应的中文段落，方便中英文对照审阅。

---

## <del style="color:red;">Research on</del> Multimodal Intelligent Recognition of <strong style="color:red;">Landslide-related</strong> InSAR <del style="color:red;">Ground</del> Deformation <del style="color:red;">Clustering Areas</del> <strong style="color:red;">Anomaly Zones</strong> <del style="color:red;">Associated with Landslide Hazards</del><strong style="color:red;">: </strong> A Case Study of Wudu District, Longnan City
> [中文对照] 滑坡隐患关联InSAR地表形变聚集区多模态智能识别研究——以陇南市武都区为例

*Author List and Affiliations Omitted for Formatting*

### Abstract
<del style="color:red;">The</del> Wudu District <del style="color:red;">of</del> <strong style="color:red;">in</strong> Longnan City, located in the West Qinling Mountains, is frequently affected by landslide disasters. Conventional InSAR <del style="color:red;">deformation</del> interpretation struggles to rapidly identify <strong style="color:red;">landslide-related</strong> <del style="color:red;">ground</del> deformation <del style="color:red;">clustering areas</del> <strong style="color:red;">anomaly zones</strong> <del style="color:red;">associated with potential landslide hazards</del>. Based on Sentinel-1A satellite data, this study <del style="color:red;">adopted</del> <strong style="color:red;">adopts the</strong> Stacking<strong style="color:red;">-</strong>InSAR <strong style="color:red;">technique</strong> to obtain ground deformation phases. <strong style="color:red;">By combining these phases</strong> <del style="color:red;">Combined</del> with multi-source remote sensing data, a multimodal sample set was constructed. The <del style="color:red;">MSegFormer</del> lightweight Transformer model<strong style="color:red;">, MSegFormer,</strong> was then <del style="color:red;">used</del> <strong style="color:red;">employed</strong> to intelligently identify landslide-related deformation <del style="color:red;">clustering areas</del> <strong style="color:red;">anomaly zones</strong>. The results <del style="color:red;">show</del> <strong style="color:red;">demonstrate</strong> that 20 <strong style="color:red;">and 71</strong> landslide-related deformation <del style="color:red;">areas</del> <strong style="color:red;">anomaly zones</strong> were identified from <del style="color:red;">the</del> ascending <strong style="color:red;">and</strong> <del style="color:red;">data and 71 from the</del> descending data<strong style="color:red;">, respectively</strong>. The proposed method effectively suppresses noise and distinguishes landslide deformation from human-induced engineering disturbances. The overall F1<strong style="color:red;">-</strong>score of the model reached 80.89%, outperforming <strong style="color:red;">comparative models such as</strong> DeepLabV3+ and Attention U<strong style="color:red;">-</strong>Net. This study demonstrates that the multimodal intelligent recognition method has <del style="color:red;">good</del> <strong style="color:red;">significant</strong> practical value in detecting potential geohazards in Wudu District, Longnan City.
> [中文对照] 摘　要： 陇南市武都区地处西秦岭山地，滑坡灾害频发，传统InSAR形变解译难以快速识别隐患关联的地表形变聚集区。本文基于Sentinel-1A卫星数据采用Stacking InSAR获取地表形变相位，结合多源遥感数据，构建多模态样本集，采用MSegFormer轻量化Transformer模型，开展了滑坡关联形变聚集区的智能识别。结果表明，升轨数据识别滑坡关联形变20处，降轨数据识别71处，该方法能有效抑制噪声、区分滑坡形变与人为工程扰动，模型整体F1值达80.89%，优于DeepLabV3+和Attention UNet。研究表明，多模态智能识别方法在陇南市武都区地质灾害隐患探测中具有良好的实用价值。

**Keywords**—InSAR; <del style="color:red;">ground</del> deformation <del style="color:red;">clustering areas</del> <strong style="color:red;">anomaly zones</strong>; landslide hazards; multimodal remote sensing; MSegFormer; Wudu District
> [中文对照] 关键词：InSAR；地表形变聚集区；滑坡隐患；多模态遥感；MSegFormer；武都区

---

### Introduction
Wudu District, Longnan City, is situated in the western section of the West Qinling Orogenic Belt<strong style="color:red;">. The region is characterized by</strong> <del style="color:red;">, where</del> intense neotectonic movements, deeply incised river valleys<strong style="color:red;">,</strong> and <strong style="color:red;">highly</strong> fragmented rock masses <del style="color:red;">are widely developed</del>. As a result, this area ranks among the most severely landslide- and debris-flow-prone regions in China [1]. Manual interpretation of potential landslide hazards <strong style="color:red;">based on</strong> <del style="color:red;">by identifying</del> InSAR-derived surface deformation <strong style="color:red;">anomaly zones</strong> suffers from low efficiency and <del style="color:red;">strong</del> <strong style="color:red;">high</strong> subjectivity<strong style="color:red;">. This approach</strong> <del style="color:red;">, which</del> can hardly satisfy the requirements for rapid and large-scale mapping of <strong style="color:red;">landslide-related</strong> surface deformation <del style="color:red;">zones</del> <strong style="color:red;">anomaly zones</strong> <del style="color:red;">associated with potential landslides</del>. Therefore, the intelligent identification of <strong style="color:red;">landslide-related</strong> InSAR surface deformation <strong style="color:red;">anomaly zones</strong> <del style="color:red;">related to potential landslide hazards</del> using multi-source remote sensing and deep learning is of great practical significance for improving the efficiency of landslide hazard detection.
> [中文对照] 1引言
陇南市武都区地处西秦岭造山带西段，新构造运动强烈，河谷深切，岩体破碎，是我国滑坡、泥石流灾害最严重的区域之一。根据InSAR地表形变聚集区人工解译滑坡隐患，效率不足且主观性强，难以满足快速、大范围识别滑坡隐患关联的地表形变聚集区需求。因此，开展基于多源遥感与深度学习的滑坡隐患关联InSAR地表形变聚集区智能识别，提升滑坡隐患识别效率具有现实意义。

Stacking-InSAR technology can effectively mitigate atmospheric delays and noise to retrieve regional surface deformation velocities, serving as a timely and important tool for potential landslide identification [2]. In recent years, deep learning has achieved remarkable progress in <strong style="color:red;">the</strong> semantic segmentation of remote sensing imagery [3]. Convolutional neural networks (CNNs) have been applied to landslide hazard recognition [4]; however, their inherent locality constrains the ability to capture contextual information. To address this limitation, attention mechanisms have been introduced to extract global feature information [5]. Vision Transformer (ViT) overcomes the drawbacks of CNNs by establishing global feature correlations and preserving spatial topological information via positional encoding [6]<strong style="color:red;">,</strong> yet it suffers from high computational complexity. The MSegFormer framework enables efficient multi-scale feature fusion, adapts to both local details and global contextual information, and is well<strong style="color:red;">-</strong>compatible with dense prediction tasks [7]. At present, studies integrating deep learning with InSAR deformation phases for potential landslide identification remain limited, mainly plagued by problems such as non-standard sample labeling, simplistic multi-modal fusion strategies, and high model sensitivity to noise.
> [中文对照] Stacking-InSAR技术能够抑制大气延迟和噪声，获取区域地表形变速率，是滑坡隐患识别的重要及时手段。近年来，深度学习在遥感图像语义分割领域取得了一定成效。卷积神经网络被应用于滑坡隐患识别，但局部特性限制了获取上下文信息的能力[。为此，引入注意力机制方法，实现全局特征信息获取。Vision Transformer（ViT）方法能够规避卷积神经网络的局限性，实现全局特征关联，通过位置编码保留空间拓扑信息，但计算复杂度较高。MSegFormer框架能够高效融合多尺度特征，适用局部细节与全局上下文信息，对密集预测任务较为兼容。当前，深度学习方法与InSAR形变相位相结合，开展滑坡隐患识别的研究较少，主要存在样本标注不规范、多模态融合简单、模型噪声敏感等问题。

In summary, in response to the practical demands of landslide hazard identification in Wudu District, Longnan City, this study employs Stacking-InSAR to obtain surface deformation velocities. A 10-band multi-modal dataset is constructed by integrating multi-source data including optical images, DEM, slope, terrain relief<strong style="color:red;">,</strong> and snow-ice coverage. The MSegFormer model is utilized to achieve pixel-level identification and classification of <strong style="color:red;">landslide-related</strong> deformation <strong style="color:red;">anomaly zones</strong> <del style="color:red;">associated with landslides</del>. Its accuracy is further compared with those of U-Net, DeepLabV3+<strong style="color:red;">,</strong> and Attention U-Net to verify the effectiveness and robustness of the proposed method. This work is expected to provide a technical reference for the intelligent identification of geological disaster hazards in complex mountainous areas.
> [中文对照] 综上，结合陇南市武都区滑坡灾害识别的现实需求，采用Stacking InSAR技术，获取形变速率，结合光学影像、DEM、坡度、地形起伏度及冰雪覆盖度等多源数据，构建10波段多模态样本集。利用MSegFormer模型，实现滑坡关联形变聚集区的像素级识别与分类；与U-Net、DeepLabV3+、Attention U-Net模型进行精度对比，验证方法的有效性与鲁棒性，为复杂山区地质灾害隐患智能识别提供技术参考。

---

### Study Area and Data
#### Study Area Overview
Wudu District is located in the southeastern part of Gansu Province, with an elevation ranging from 660 to 3600 m. The terrain is high in the northwest and low in the southeast, characterized by steep mountains and intensely incised gullies. The climate is a humid subtropical monsoon climate <del style="color:red;">in the northern subtropical zone</del>, with an annual precipitation of 400–800 mm and concentrated rainstorms. The geological structure is complex, as the district lies at the junction of three major tectonic units in the western segment of the Qinling Orogenic Belt. Fractured rock masses and widespread weak strata, combined with human engineering activities such as slope cutting for construction and road building, have resulted in frequent occurrences of landslides and debris flows.
> [中文对照] 2 研究区与数据
2.1 研究区概况
武都区地处甘肃省东南部，海拔660~3600 m，地势西北高东南低，山势陡峻，沟谷切割强烈。气候属北亚热带湿润季风气候，多年降水量400~800 mm，暴雨集中。地质构造复杂，位于秦岭造山带西段三大构造单元交接处，岩体破碎，软弱岩层广布，加之削坡建房、道路建设等人类工程活动，导致滑坡、泥石流灾害频发。

#### Data Sources and Preprocessing 
In this study, Sentinel-1A SAR images from 2021 to 2023, GF-1/GF-2 multispectral imagery, and ALOS World 3D DEM data were employed. All data were unified to the WGS-84 coordinate system and resampled to <strong style="color:red;">a</strong> 10 m resolution. The average annual surface deformation velocity was obtained using the Stacking<strong style="color:red;">-</strong>InSAR technique. A 9-band multi-modal dataset was constructed, including ascending/descending InSAR deformation phases (3 bands), RGB optical imagery (3 bands), elevation, slope, and terrain relief.
> [中文对照] 2.2 数据源与预处理
研究使用2021 – 2023年Sentinel-1A SAR数据、高分一号/二号多光谱影像、ALOS World 3D DEM数据，数据统一至WGS‑84坐标系，重采样至10 m。采用Stacking InSAR技术获取年度平均地表形变速率。构建InSAR升/降轨形变相位（3波段）、RGB光学（3波段）、高程、坡度、地形起伏度9波段多模态数据集。

---

### Methodology 
Surface deformation phases were obtained using Stacking-InSAR and fused with multi-source remote sensing data. Under a three-dimensional visualization environment, visual interpretation was conducted to construct a pixel-level sample set consisting of three categories: landslide-related deformation, non-landslide deformation, and non-deformation regions. Subsequently, standard HDF5 format datasets were generated through positive–negative sample balancing, data augmentation, and stratified sampling. Finally, a multi-modal intelligent recognition model based on MSegFormer was established and trained with 10-band data as input. The proposed model was applied to intelligent recognition in Wudu District, Longnan City, and its accuracy was compared with that of DeepLabV3+, U<strong style="color:red;">-</strong>Net, and Attention U<strong style="color:red;">-</strong>Net.
> [中文对照] 3 方法
3.1 技术路线
基于Stacking -InSAR获取地表形变相位，融合多源遥感数据，在三维环境下由目视解译，构建滑坡关联形变、非滑坡关联形变、非形变三类的像素级样本集；然后通过正负样本平衡、数据增广、分层抽样，形成标准化HDF5格式样本集；最后构建MSegFormer多模态智能识别模型，以10波段数据为输入进行训练与优化，以陇南市武都区开展只能识别应用，并与DeepLabV3+、UNet、Attention UNet对比精度。

#### Stacking Technique
The Stacking technique combines multiple interferograms to address the problems of interferometric decorrelation and atmospheric delay inherent in conventional InSAR, thereby enabling the estimation of regional surface deformation velocities. As one of the most fundamental algorithms for multi-temporal InSAR, Stacking estimates the linear phase rate using multiple unwrapped differential interferograms. This process essentially constitutes a linear regression of N groups of observations based on the least squares method, with the estimation formula expressed as follows:

<strong style="color:red;">where $\Delta t$ is the temporal baseline of the interferogram; $\Delta \phi$ is the unwrapped differential interferometric phase; and $v$ is the linear phase velocity.</strong>
> [中文对照] 3.2 Stacking InSAR形变相位提取
Stacking技术通过组合多个干涉图的方法，主要解决常规InSAR面临的干涉失相干和大气延迟的问题，以实现区域形变速率的获取，是多时相InSAR技术最基础的一种算法。Stacking技术通过生成的多景差分干涉解缠图估算线性相位速率，实际是基于最小二乘法对N组观测值线性回归的过程，估算公式为：
式中：为干涉图的时间基线；为解缠的差分干涉相位；为线性相位速率。

#### **Architecture of the MSegFormer Model**
MSegFormer is a lightweight Transformer-based semantic segmentation model. It was proposed to address the limitations of Vision Transformer (ViT) in prediction tasks, including fixed feature resolution, positional encoding interpolation errors, excessive computational complexity, and difficulty in directly fusing multi-source data. Based on the SegFormer architecture, MSegFormer is adapted and reconstructed for multi-channel inputs including multi-temporal InSAR deformation phases, multispectral images, and DEM data. The model mainly consists of three components: overlapping patch embedding, a hierarchical Transformer encoder, and a lightweight all-MLP decoder.
> [中文对照] 3. 3MSegFormer智能识别模型
MSegFormer是一种轻量级Transformer语义分割模型，是针对Vision Transformer（ViT）在预测任务中特征分辨率固定、位置编码插值损失及计算复杂度过高及难以直接融合多源数据的问题提出的。MSegFormer模型在SegFormer架构基础上，针对多InSAR形变相位、多光谱影像、DEM通道输入进行了适配和重构。主要包含重叠图像块嵌入、分层Transformer编码器和轻量级全MLP解码器三部分。

**Overlap Patch Embeddings**
MSegFormer adopts overlapping patch merging<del style="color:red;">,</del> and constructs a hierarchical feature structure using convolutional layers (kernel = 7, stride = 4, padding = 3) and LayerNorm. The overlap between adjacent patches preserves local spatial continuity and enlarges the receptive field.
> [中文对照] （1）Overlap Patch Embeddings（重叠图像块嵌）
MSegFormer采用重叠图像块合并，使用卷积层（kernel=7, stride=4, padding=3）和LayerNorm构建特征层级结构。相邻图像块间的重叠，保留了区域局部连续性，扩大了感受野。

**Hierarchical Transformer Encoder**
The hierarchical Transformer encoder serves as the core component of MSegFormer. First, the first-stage embedding layer is reconstructed by dynamically instantiating nn.Conv2d and setting the number of input channels `in_channels` as a configurable parameter, thereby supporting multi-source data with arbitrary channel numbers. The encoder then consists of four consecutive Transformer blocks (Block1 to Block4), each outputting feature maps at different resolutions. In addition, the feed-forward network within the encoder adopts a Mixed Feed-Forward Network (Mix-FFN), which integrates convolutional and linear feed-forward structures on the basis of the traditional Feed-Forward Network (FFN):

*(Equation 2)*

where $x$ denotes the features derived from the self-attention module. By introducing a convolutional structure, Mix-FFN enables the model to further capture spatial information. This design enhances spatial feature modeling while maintaining a global receptive field.
> [中文对照] （2）分层Transformer编码器
分层Transformer编码器是MSegFormer的核心组件。首先，通过动态实例化nn.Conv2d，将输入通道数in_channels设为可配置参数重构第一阶段嵌入层，从而支持任意通道数的多源数据；然后，编码器由四个连续的Transformer模块（Block1~Block4）构成，每个模块输出不同分辨率的特征图。另外，编码器中的前馈网络采用了混合前馈网络（Mix-FFN），其在传统Feed-Forward Network（FFN）的基础上整合了卷积（Convolution）和线性（Linear）两种前馈神经网络结构：
其中，是来自自注意模块的特征。通过引入卷积结构，Mix-FFN能让模型进一步考虑空间信息。该设计在保持全局感受野的同时增强了空间特征建模能力。

**Lightweight All-MLP Decoder**
MSegFormer employs a lightweight decoder composed exclusively of MLP layers. Multi-level features from the encoder are first unified in <strong style="color:red;">the</strong> channel dimension via an MLP layer. These features are then upsampled to 1/4 resolution, concatenated, and fused using another MLP layer. Finally, the fused features are fed into a subsequent MLP layer to predict the segmentation mask with a resolution of H×W×C, where C denotes the number of object categories.
> [中文对照] （3）轻量级全MLP解码器
MSegFormer使用了一个轻量级的解码器，该解码器仅由MLP层组成。编码器的多级特征通过一个MLP层进行通道维度统一，特征被上采样到1/4大小，并进行拼接，采用MLP层来融合拼接后的特征，最后，另一个MLP层将融合后的特征输入，预测分割掩码，分辨率为，其中是类别的数量。

#### Precision Evaluation Indicators
Precision, Recall, F1-Score, and mean Intersection over Union (mIoU) are adopted as the evaluation indicators to assess the performance of the segmentation model. For a single category, True Positives (TP) refer to the pixels that are correctly identified and classified, False Positives (FP) represent the pixels that are incorrectly recognized as the target category, and False Negatives (FN) denote the pixels of the target category that are missed and not identified.

The final precision is evaluated by the macro-average of F1-Scores of three categories, namely landslide-related deformation, non-landslide-related deformation, and non-deformation. The calculation formula of the macro-average F1-Score is defined as follows:

*(Equation 3)*
> [中文对照] 3.4精度评价指标
采用Precision、Recall、F1-Score和mIoU作为评价指标。对于单类，TP为正确识别像元，FP为误识别，FN为漏识别。最终精度采用三类滑坡关联形变、非滑坡关联形变、非形变F1的宏平均：

---

### Results and Analysis
#### Comparison of Model Performance
On the test set of Wudu District, the proposed MSegFormer is compared with DeepLabV3+, U<strong style="color:red;">-</strong>Net, and Attention U<strong style="color:red;">-</strong>Net. All models adopt the same 10-band multimodal input and training strategy. The quantitative results are presented in Table 1.

<del style="color:red;">SegFormer</del> <strong style="color:red;">The proposed MSegFormer</strong> achieves an F1-score 4.81 percentage points higher and an mIoU 5.4 percentage points higher than Attention U<strong style="color:red;">-</strong>Net, with Precision and Recall reaching 86.35% and 76.64%, respectively. This indicates that the proposed method can better balance precision and recall. U<strong style="color:red;">-</strong>Net exhibits the poorest performance, showing weak capability in capturing the complex spatial information of InSAR deformation. Although DeepLabV3+ yields relatively high precision, it suffers from low recall and severe missed detections. Benefiting from global self-attention and multi-scale feature representation, MSegFormer achieves the optimal overall performance.
> [中文对照] 4 结果与分析
4.1 模型性能对比
在武都区测试集上，将MSegFormer与DeepLabV3+、UNet、Attention UNet进行对比，所有模型均采用相同的10波段多模态输入和训练策略。定量结果如表1所示。
M egFormer的F1值比Attention UNet提高4.81个百分点，mIoU提高5.4个百分点，Precision和Recall分别达到86.35%和76.64%，表明该方法能较好地平衡准确率与召回率。UNet表现最差，捕捉InSAR形变的复杂空间信息能力较弱。DeepLabV3+虽有较高Precision但Recall偏低，漏检较多。MSegFormer具有全局自注意力和多尺度特征，发挥了最优性能。

#### Identification Results of Deformation <del style="color:red;">Concentration Zones</del> <strong style="color:red;">Anomaly Zones</strong> in Wudu District
The MSegFormer model is applied to identify deformation <strong style="color:red;">anomaly</strong> zones in Wudu District, and the results are illustrated in Fig. 2. A total of 71 deformation <del style="color:red;">concentration zones</del> <strong style="color:red;">anomaly zones</strong> are identified from descending orbit data, among which 69 are landslide-related deformations and 2 are non-landslide deformations induced by engineering activities. For ascending orbit data, 20 deformation <strong style="color:red;">anomaly</strong> zones are detected, all of which are landslide-related. The deformation anomalies are generally distributed in dense belts in the northwest of the urban area, extending southeastward along the Bailong River, which is highly correlated with regional geological structures and fluvial erosion. The number of deformations identified by the descending orbit is larger than that by the ascending orbit, indicating that the main deformation direction in this region is more consistent with the line-of-sight direction of the descending orbit, which demonstrates the necessity of multi-orbit InSAR observations.
> [中文对照] 4.2 武都区形变聚集区识别结果
应用MSegFormer模型对武都区进行识别，结果如图2所示。降轨数据共识别形变聚集区71处，其中69处为滑坡关联形变，2处为工程活动引起的非滑坡形变；升轨数据识别20处，均为滑坡关联形变。形变异常总体呈带状密集分布于城区西北部，沿白龙江向东南延伸，与区域地质构造和河流侵蚀作用高度相关。降轨识别的形变数量多于升轨，表明该区域主要形变方向与降轨雷达视线向更为一致，体现了多轨道观测的必要性。

**Landslide-Related Deformation Identification:** Figure 3 presents two typical landslide cases. Case 1 is located on a gentle slope on the left bank of the Bailong River, where the InSAR deformation phase exhibits a typical concentrated deformation pattern. Optical images reveal farmland reconstructed from an ancient landslide with dense villages, which is consistent with existing survey results. Case 2 is situated on the deeply incised mountain sidewall on the right bank of the Bailong River in western Wudu District, with obvious deformation characteristics and clear landslide boundaries in optical images. Although the InSAR deformation is subject to strong noise interference, the proposed method shows outstanding performance in noise suppression and accurately identifies the deforming landslide in this region, satisfying the application requirements of wide-area intelligent identification.
> [中文对照] （1）滑坡关联形变识别。图3展示了2个典型滑坡案例。案例一位于白龙江左岸平缓斜坡，InSAR形变相位呈典型的变形聚集形态，光学影像显示为老滑坡改造的农田，村落密集，与已有调查成果吻合。案例二位于武都区西部白龙江右岸山区河流深切割山体侧壁，形变特征显著，光学影像滑坡边界清晰，InSAR形变噪声干扰较为强烈，从结果上看，噪声抑制方面表现突出，较好的识别出该区域变形滑坡，确保了广域智能识别的应用需求。

**Discrimination <del style="color:red;">ability</del> <strong style="color:red;">Ability</strong> for <del style="color:red;">nonlandslide deformations</del> <strong style="color:red;">Non-Landslide Deformations</strong>:** Two non<strong style="color:red;">-</strong>landslide<strong style="color:red;">-</strong>related deformations are identified by the model from descending orbit data. Verified by optical imagery, both are located at construction sites in the urban area with flat terrain, and the deformations show a local funnel<strong style="color:red;">-</strong>shaped pattern, which is significantly different from the slope deformation mode of landslides. This indicates that MSegFormer can effectively use topographic and optical features to distinguish deformations caused by human engineering activities from landslide deformations.
> [中文对照] （2）非滑坡形变区分能力。在降轨数据中，模型识别出2处非滑坡关联形变。经光学核实，均位于城区在建工地，地势平坦，形变呈局部漏斗状，与滑坡的斜坡单元形变模式明显不同，表明MSegFormer能有效利用地形和光学特征区分人为工程活动与滑坡形变。

**Noise <del style="color:red;">suppression</del> <strong style="color:red;">Suppression</strong> and <del style="color:red;">dense target identification</del> <strong style="color:red;">Dense Target Identification</strong>:** The descending orbit data over Wudu District are strongly affected by noise, posing great difficulties for traditional manual interpretation. Relying on global self<strong style="color:red;">-</strong>attention and hierarchical feature fusion, MSegFormer suppresses noise while successfully identifying densely distributed deformation targets, such as multiple deformation <strong style="color:red;">anomaly</strong> zones on deeply incised mountain flanks in mountainous areas, some of which contain residential settlements and were unrecorded in previous surveys. The efficient noise suppression capability of the model provides support for the rapid screening of wide<strong style="color:red;">-</strong>area geological disaster hazards.
> [中文对照] （3）噪声抑制与密集目标识别。武都区降轨数据噪声干扰强烈，传统人工解译难度大。MSegFormer凭借全局自注意力和分层特征融合，在抑制噪声的同时成功识别出密集分布的形变目标，例如位于山区河流深切割山体侧壁的多个形变区，部分区域有居民点，此前未被调查记录。模型的高效噪声抑制能力为广域地质灾害隐患快速筛查提供了支撑。

---

### Discussion
This study integrates InSAR deformation phase and multi-source remote sensing data, and employs the MSegFormer model to realize intelligent identification of <strong style="color:red;">landslide-related</strong> deformation <del style="color:red;">concentration zones</del> <strong style="color:red;">anomaly zones</strong> <del style="color:red;">associated with potential landslide hazards</del>. The results demonstrate that multi-modal data (topography, optical imagery, etc.) are crucial for distinguishing landslide deformations from anthropogenic engineering disturbances, and relying solely on InSAR tends to cause misjudgment. The proposed MSegFormer achieves an F1-score of 80.89%, outperforming DeepLabV3+ and Attention U<strong style="color:red;">-</strong>Net. Benefiting from the global self-attention mechanism and multi-scale feature extraction capability of <strong style="color:red;">the</strong> Transformer <strong style="color:red;">architecture</strong>, the model can effectively capture irregular deformation boundaries and maintain robustness under strong noise conditions. The discrepancy in the number of identified deformations between ascending and descending orbits (71 from descending orbit and 20 from ascending orbit) reflects that the dominant deformation direction in the study area is more consistent with the line-of-sight direction of the descending orbit, verifying the necessity of multi-orbit observations. The model successfully identifies numerous weak deformation signals and previously unrecorded deformation <strong style="color:red;">anomaly</strong> zones, exhibiting favorable noise suppression and preliminary screening performance. Limitations of this work include subjectivity in sample labeling, spatial scale mismatch among multi-source data, and the lack of consideration for non-linear deformations. Future work will expand the cross-regional sample database and introduce time-series InSAR features to improve the generalization and practicality of the model.
> [中文对照] 5 讨论
本研究融合InSAR形变相位与多源遥感数据，利用MSegFormer模型实现了滑坡隐患关联形变聚集区的智能识别。结果表明，多模态数据（地形、光学等）对区分滑坡形变与人为工程扰动至关重要，单靠InSAR易误判。MSegFormer的F1值达80.89%，优于DeepLabV3+和Attention UNet，得益于Transformer的全局注意力与多尺度特征提取能力，能有效捕捉不规则形变边界并在强噪声下保持稳健。升降轨识别数量差异（降轨71处，升轨20处）反映研究区形变主方向与降轨视线向更为一致，证实多轨道观测的必要性。模型成功识别了多处微弱信号及以往遗漏的形变区，展现出良好的噪声抑制与初筛能力。局限性包括样本标注主观性、多源数据空间尺度不匹配及未考虑非线性形变。后续将扩展跨区域样本库并引入时序InSAR特征，以提升模型泛化性与实用性。

---

### Conclusion
Taking Wudu District of Longnan City as a typical demonstration area, this study obtains surface deformation phase based on Stacking<strong style="color:red;">-</strong>InSAR, constructs a 10-band multimodal dataset by fusing multi-source remote sensing data, and adopts the lightweight Transformer model MSegFormer to intelligently identify <strong style="color:red;">landslide-related</strong> InSAR surface deformation <del style="color:red;">concentration zones</del> <strong style="color:red;">anomaly zones</strong> <del style="color:red;">associated with potential landslide hazards</del>. On the test set of Wudu District, MSegFormer achieves an F1-score of 80.89% and an mIoU of 70.28%, outperforming DeepLabV3+, U<strong style="color:red;">-</strong>Net and Attention U<strong style="color:red;">-</strong>Net, which verifies the superiority of the Transformer architecture in multi-source remote sensing data fusion and landslide deformation recognition. The model is applied to identify 20 landslide-related deformations from ascending orbit data and 71 from descending orbit data, and can effectively distinguish landslide deformations from anthropogenic engineering disturbance deformations, demonstrating its practical value in detecting geological disaster hazards in complex mountainous areas. With favorable transferability and operational potential, the proposed method can provide technical support for the regular hazard identification, monitoring<strong style="color:red;">,</strong> and early warning in landslide-prone regions of the West Qinling Mountains.
> [中文对照] 6 结论
本文以陇南市武都区为典型示范区，基于Stacking InSAR获取地表形变相位，融合多源遥感数据构建10波段多模态样本集，采用轻量化Transformer模型MSegFormer开展了滑坡隐患关联InSAR地表形变聚集区的智能识别。MSegFormer在武都区测试集上取得了80.89%的F1值和70.28%的mIoU，优于DeepLabV3+、UNet和Attention UNet，验证了Transformer架构在多源遥感数据融合与滑坡形变识别任务中的优越性。应用模型识别出升轨滑坡关联形变20处、降轨71处并能有效区分滑坡形变与人为工程扰动形变，展示了在复杂山区地质灾害隐患探测中的实用价值。具有可迁移性和业务化潜力，可为西秦岭滑坡灾害高发区的常态化隐患识别与监测预警提供技术支撑。

---

*(Acknowledgments and References follow original text)*

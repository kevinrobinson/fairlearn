## Vision
On a high level, we firmly view fairness as a socio-technical challenge, so we want to provide techniques that enable humans to navigate fairness trade-offs in a manner that makes most sense for their context. Because of this, our package includes not only algorithm and metrics, but also the fairness assessment dashboard--and we hope that the development of UX for fairness assessment / unfairness mitigation will be our key area of contribution [fairlearn#311](https://github.com/fairlearn/fairlearn/issues/311#issuecomment-592716247).  Historically, the project started as a Python package that implements algorithms for mitigating unfairness in supervised machine learning.

Fairness is fundamentally a sociotechnical challenge. Many aspects of fairness, such as justice and due process, are not captured by quantitative fairness metrics. Furthermore, there are many quantitative fairness metrics which cannot all be satisfied simultaneously. Our goal is to enable humans to assess different mitigation strategies and then make trade-offs appropriate to their scenario ([README.md](https://github.com/fairlearn/fairlearn#what-we-mean-by-fairness), [fairlearn#244](https://github.com/fairlearn/fairlearn/issues/244#issuecomment-575309920)).  To this point, 

One big source of concern for us is how the issue of fairness is presented in our package (documentation and any other materials) - we do not want to enable so-called 'fairwashing' of ML algorithms ([fairlearn#406](https://github.com/fairlearn/fairlearn/issues/406#issuecomment-623541578)).

While we have included example notebooks, these often emphasis the mechanics of interacting with the API rather than actual use cases dealing with fairness as a sociotechnical challenge ([fairlearn-proposals#2](https://github.com/fairlearn/fairlearn-proposals/issues/2#issuecomment-594941077)).  Moving forward, any documentation and examples of a fairness toolkit should take into account an entire range of concerns due to the sociotechnical nature of fairness. The showcased notebooks will provide the space to cover scenarios in depth. The focus is not only on showing example usage of the Fairlearn toolkit, but on how to approach fairness in ML in general. We may want to add a scenario even if it contains only few of Fairlearn's capabilities, but it otherwise demonstrates a great example of how to build AI responsibly ([fairlearn-proposals#8](https://github.com/fairlearn/fairlearn-proposals/pull/8/files#diff-21173c05e65dcf529aa6c8cbc26bf0e9R104)).


## Important prior research
These papers are important because they describe mitigation algorithms implemented in this library (see also [README.md#fairlearn-algorithms](https://github.com/fairlearn/fairlearn#fairlearn-algorithms)):
- [A Reductions Approach to Fair Classification (Agarwal et al. 2018)](https://arxiv.org/abs/1803.02453)
- [Fair Regression: Quantitative Definitions and Reduction-based (Algorithms Agarwal et al. 2019)](https://arxiv.org/abs/1905.12843)

This paper describes framing language for different technical conceptualizations of fairness metrics:
- [Equality of Opportunity in Supervised Learning (Hardt et al. 2016)](https://arxiv.org/abs/1610.02413)

These papers describe HCI research on practioners' needs around fairness assessment and mitigation:
- [Improving Fairness in Machine Learning Systems: What Do Industry Practitioners Need? (Holstein et al. 2019](https://arxiv.org/pdf/1812.05239.pdf)
- [Co-Designing Checklists to Understand Organizational Challenges and Opportunities around Fairness in AI (Madaio et al. 2020)](http://www.jennwv.com/papers/checklists.pdf).


## Related projects
- [tensorflow/fairness-indicators](https://github.com/tensorflow/fairness-indicators), [What-If Tool](https://arxiv.org/pdf/1907.04135.pdf), [TFCO](https://github.com/google-research/tensorflow_constrained_optimization/blob/master/README.md)
- [IBM/aif360](https://github.com/IBM/aif360), [Bellamy et al. (2019)](https://arxiv.org/abs/1810.01943)
- [scikit-fairness](https://github.com/koaning/scikit-fairness)
- [FairVis (Cabrera et al. 2019)](https://arxiv.org/pdf/1904.05419.pdf)
- [uber/manifold](https://github.com/uber/manifold) (eg, comparing models)


## Who we serve
We are looking to enable practitioners (in tech, but also other sectors) to effectively do fairness assessment and mitigation.  The field of fair ML is dynamically evolving, so we expect to interact with academic research.  Not just the academic research on new algorithms, but also academic research on how practitioners use these algorithms. Some of the people on the Fairlearn team have been involved in that style of research ([fairlearn#406](https://github.com/fairlearn/fairlearn/issues/406#issuecomment-623597208)).

We are still in a fairly early stage of moving from being a research project to a more general tool, and we have not finalised how we want to fit into the larger ecosystem ([fairlearn#406](https://github.com/fairlearn/fairlearn/issues/406#issuecomment-623541578)).  To this point we have focused on the `scikit-learn` community, and our API design emphasizes consistency and compatibility with its conventions ([CONTRIBUTING.md#unfairness-mitigation-algorithms](https://github.com/fairlearn/fairlearn/blob/master/CONTRIBUTING.md#unfairness-mitigation-algorithms)).

As the FAT-ML community works on the topic and advancements are made, it'd be nice to have the methods available to a broader community for us to see the feedback, what works, and what doesn't in practice. ([fairlearn#311](https://github.com/fairlearn/fairlearn/issues/311#issuecomment-592401451)).  We are still at the early stages of transitioning from a research project and building a community of users.


## How we contribute
We aspire to contribute by creating: tools, visualizations and algorithms for fairness assessment and unfairness mitigation.  As the project grows, we may explore domain-specific use cases and create guides for when to use various tools, metrics, algorithms or visualizations ([fairlearn-proposals#2](https://github.com/fairlearn/fairlearn/issues/311#issuecomment-592716247), [fairlearn#311](https://github.com/fairlearn/)), although to this point the approaches and tools are mostly generic and abstract ([fairlearn-proposals#2](https://github.com/fairlearn/fairlearn-proposals/issues/2#issuecomment-594941077)).



## How we work
Our hope is to be truly open and collaborative ([fairlearn#311](https://github.com/fairlearn/fairlearn/issues/311#issuecomment-592716247)).
We think that having more eyes and ideas on the same package makes it stronger, and creates a much nicer and more resilient codebase and workflow.
We'd love to move fairlearn towards having a "developer community" ([fairlearn#406](https://github.com/fairlearn/fairlearn/issues/406#issuecomment-623650648)
Please come join us in [Gitter](https://gitter.im/fairlearn/community)!


## What feels like success
- ???
- ???
- ???
- shipping more metrics?
- increased usage and adoption?
- proof-of-concept UX for considering sociotechnical angles?
- addressing specific use needs in papers on practitioner needs?
- contributions that could be shaped in academic publications?


## Roadmap
Over the next three months, we are mostly invested in the technical infrastruture of the project, including:
- Improves the consistency of the Metrics API (https://github.com/fairlearn/fairlearn-proposals/pull/1, https://github.com/fairlearn/fairlearn-proposals/issues/5, https://github.com/fairlearn/fairlearn-proposals/pull/9, https://github.com/fairlearn/fairlearn-proposals/pull/6)
- Improve CI setup (https://github.com/fairlearn/fairlearn-proposals/pull/7)
- Improve project documentation (https://github.com/fairlearn/fairlearn-proposals/pull/8/files#diff-21173c05e65dcf529aa6c8cbc26bf0e9R104)

In the next year, we hope to serve our users by:
- ???
- ???
- ???

*COMMENT: The [milestones](https://github.com/fairlearn/fairlearn/milestones) page has drifted a bit:
- Improve Testing
- Improve Documentation
- Short-term API improvements
- Scalability exploration & improvements
- Add more disparity metrics
- Address user feedback on visualizations
- Integration with scikit-learn
- Support multiple sensitive features
- Fair Regression with ExponentiatedGradient*


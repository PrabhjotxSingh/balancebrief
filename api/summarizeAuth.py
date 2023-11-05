import cohere
import numpy as np

co = cohere.Client('lqJD3VjaVUpo4tgxxzg2RFIuu6p3jXmmezQc0tXD')
article = "China will double down on power system reforms and shift its focus to reducing carbon emissions, a Communist Party policymaking body said late on Tuesday, without giving further details. The party's commission for deepening reform, an agency responsible for accelerating priority reforms for the leadership, outlined broad proposals for opening up the economy, including the latest effort to improve the country's power networks and oil and natural gas markets, state broadcaster CCTV reported. China has previously launched several rounds of power sector reforms to improve efficiency, lower electricity prices, and rationalize coal power investment, with the aim of reducing costs for end users that weigh on economic activity. It will now make further changes in hopes of accelerating the construction of a power system that is economically efficient, flexible and intelligent in supply and demand coordination, the commission said following a meeting. However challenges remain, including provincial government protectionism and a lack of inter-provincial coordination, as well as other regulatory hurdles. Fixed, long-term power trading agreements also limit flexibility in the system.During a drought in August 2022, fixed, unidirectional power trading agreements forced hydro-dependent southwestern Sichuan province to export power out of the province to fulfil these contracts, even as consumers in the province endured power cuts.China must also gradually shift its focus from controlling energy consumption to controlling its carbon emissions, the commission said.No further details were provided on how the shift would be implemented.China has set targets to cut carbon dioxide intensity by 18% between 2021 and 2025, and energy intensity by 13.5% in the same period. However it has not set any targets on carbon dioxide emissions.In the oil and gas markets, China will focus on improving national oil and gas security capabilities ... and ensure stable and reliable supply, the commission also said.The proposals come amid an intensified focus on domestic energy security in the country, which is the world's largest crude oil importer.Andrew reports on energy and energy policy in China. He previously worked in investment banking in London, covering European high-yield debt transactions. Andrew speaks Mandarin and is learning Russian. U.S. companies have announced plans to build dozens of solar panel factories across the country since last year when President Joe Biden’s signature climate law unleashed billions of dollars of subsidies, raising hopes a clean energy boom can provide tens of thousands of good paying jobs. Wind and solar power are booming in China and may help limit global carbon emissions far faster than expected, according to a new study.Solar panel installations alone are growing at a pace that would increase global capacity by 85% by 2025. The report says the country's green energy targets for 2030 look set to be exceeded five years ahead of schedule.But coal plants are also increasing, partly as backup for all the new wind and solar farms, the authors say.China is often seen as the key to the world's efforts to rein in the carbon emissions that are the root cause of climate change. The country is the world's biggest user of coal, mainly for making electricity. The use of coal is responsible for around 69% of China's emissions of carbon dioxide.But this new study shows that China is fast building up capacity to generate power from wind and solar, which could have a significant impact on limiting the impacts of rising temperatures.The research has been carried out by Global Energy Monitor (GEM), an independent research group whose work is often used by the World Bank, the International Energy Agency and governments.The report looks at China's current installed green energy capacity, but also makes projections on what's been announced and in construction over the next two years. It finds that right now China has more solar panels installed in large-scale projects than the rest of the world combined. On wind energy, the country has doubled its capacity since 2017. But this appears to be only the start. According to GEM, China is expanding this sector rapidly and will more than double its capacity for wind and solar by the end of 2025.This would see China increase the global wind turbine fleet by 50%, and increase the world's large-scale solar installations by 85% compared to current levels. This current surge is the end-product of plans dating back over two decades.  In that time China has become the world's leading supplier of solar panels, driving down costs all across the supply chain. That has helped make solar and wind installations in China economically competitive.  Subsidies have played their part, as have regulations requiring each province to hit green energy targets. While over half a trillion dollars was spent worldwide on wind and solar last year, China accounted for 55% of that. Back in 2020, President Xi Jinping said that China would install over 1,200 gigawatts of solar and wind power by 2030. This new report says this target will be surpassed five years ahead of schedule. We believe that the surge in building renewables certainly provides a basis for peaking [Chinas] carbon emissions earlier than 2030, said Martin Weil, one of the reports authors.But while this could be significant news for limiting global warming, Chinas coal use remains a major challenge. In 2022, China built approximately two new coal fired power stations every week - many of these were located on new solar and wind parks, often to provide back up power and to ensure continuity of energy supply. The big issue going forward is how will these coal plants actually be deployed,Mr Weil said. One hopes that theyre deployed in a way that that puts the ratio of renewables to coal as high as possible.Other key indicators will be the development of battery storage and the growth of hydrogen - both will be important in helping China transition successfully away from coal.The European Union’s climate chief on Monday expressed concern over the expansion of China’s coal industry, with the building of new coal-fired plants. At a conference in Beijing, Frans Timmermans said that while China is forging ahead with plans to expand its use of renewable resources such as wind and solar energy, the country has also been constructing an ever-growing number of coal-fired plants in the past few years. “And that seems to be in a contradiction and it is in contradiction,” said Timmermans. “But at the same time, I do understand the anxiety caused by potential blackouts.”China is the world’s biggest and fastest-growing producer of renewable energy. It aims to turn one-third of its total power supply renewable by 2025.As more cities are experiencing sweltering temperatures this summer, the country may face power shortages and challenges to electricity grids, similar to what happened last year. At the same time, water shortages have led to reductions in hydropower generation. China’s climate envoy Xie Zhenhua attended the conference and presented a commemorative plate to Timmermans, who is on a two-day visit to China for the EU-China High-level Environment and Climate Dialogue.Official plans called for boosting coal production capacity by 300 million tons last year, at least the third consecutive year of growth. Although China is one of the biggest investors in wind and solar, anxious leaders called for more coal-fired power after economic growth plunged and shortages caused blackouts and factory shutdowns. Russia’s attack on Ukraine added to the anxiety that foreign oil and coal supplies might be disrupted. China is the top producer and consumer of coal. Global trends hinge on what Beijing does.The Communist Party has rejected binding emissions commitments, citing its economic development needs. Beijing has avoided joining governments that promised to phase out the use of coal-fired power.China has said carbon emissions will peak by 2030 and the country will become carbon neutral by 2060 by planting trees and through other offsets. Some European and American officials have called on China to adopt more ambitious targets. China accounts for 26.1% of global emissions, more than double the U.S. share of 12.8%."


#Encode your query with input type 'search_query'
query = "Co2 Emission in China"
query_emb = co.embed([query], input_type="search_query", model="embed-english-v3.0").embeddings
query_emb = np.asarray(query_emb)
query_emb.shape



def summarize(co, query, text):
    complete = []

    response1 = co.summarize(
        text=text,
        format= 'paragraph'
    )

    complete.append(response1.summary)

    response2 = co.summarize(
        text=text,
        format= 'paragraph'
    )

    complete.append(response2.summary)

    response3 = co.summarize(
        text=text,
        format= 'paragraph'
    )

    complete.append(response3.summary)

    response4 = co.summarize(
        text=text,
        format= 'paragraph'
    )

    complete.append(response4.summary)

    response5 = co.summarize(
        text=text,
        format= 'paragraph'
    )
    complete.append(response5.summary)

    # print(complete)


    #Encode your documents with input type 'search_document'
    complete_emb = co.embed(complete, input_type="search_document", model="embed-english-v3.0").embeddings
    complete_emb = np.asarray(complete_emb)



    #Compute the dot product between query embedding and document embedding
    scores = np.dot(query, complete_emb.T)[0]

    #Find the highest scores
    max_idx = np.argsort(-scores)

    print(complete[max_idx[0]])

    return complete[max_idx[0]]


new_summary = summarize(co, query_emb, article)
print("New summary: " + new_summary)
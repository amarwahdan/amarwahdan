from math import cos, sin, pi

TOOLS = [
    ('python','Python','#f9cd5b','MODEL DEVELOPMENT','Build pipelines. Coordinate agents. Connect data to decisions.','pipeline.compose()','model',['mooox','health-guardian','amarzero','tactical','qorabot','sentiment']),
    ('pytorch','PyTorch','#ee7758','MODEL DEVELOPMENT','Train neural models. Learn dynamics. Connect prediction to planning.','world_model.predict()','model',['health-guardian','amarzero']),
    ('tensorflow','TensorFlow','#ffa947','MODEL DEVELOPMENT','Develop neural image classifiers and applied learning workflows.','model.fit()','model',[]),
    ('scikitlearn','scikit-learn','#efad5d','CLASSICAL MACHINE LEARNING','Turn sparse text features into a fitted probabilistic classifier.','classifier.predict()','model',['sentiment']),
    ('opencv','OpenCV','#88dc7c','VISUAL INTELLIGENCE','Read frames. Process visual signals. Explore object tracking.','frame.observe()','vision',['amarzero']),
    ('huggingface','Hugging Face','#ffd75e','LANGUAGE & MULTIMODAL MODELS','Connect pretrained models to perception, retrieval, and generation.','transformer.generate()','model',['health-guardian','qorabot','sentiment']),
    ('langchain','LangChain','#8edeb7','RETRIEVAL SYSTEMS','Carry context and source metadata through retrieval and generation.','retriever.invoke()','retrieval',['qorabot']),
    ('crewai','CrewAI','#ff7e7b','AGENTIC WORKFLOWS','Explore coordinated roles and multi-agent workflow design.','agents.coordinate()','agents',[]),
    ('google','Google ADK','#8ebdff','AGENTIC WORKFLOWS','Build tool-oriented agent workflows with explicit execution steps.','tool.call()','agents',[]),
    ('ollama','Ollama','#e5eae8','MODEL EXECUTION','Connect local language-model execution to agent tooling.','model.route()','runtime',['mooox']),
    ('docker','Docker','#57b7fa','EXECUTION BOUNDARIES','Isolate security tools in reproducible container environments.','sandbox.run()','runtime',['mooox']),
    ('numpy','NumPy','#88b0df','NUMERICAL REPRESENTATION','Represent motion, numerical state, and analytical features.','state.vectorize()','model',['amarzero','tactical']),
    ('pandas','pandas','#b3a6ee','DATA & FEATURE ENGINEERING','Clean records. Deduplicate chains. Construct feature matrices.','features.transform()','retrieval',['amarzero','tactical','qorabot','sentiment']),
    ('gradio','Gradio','#ffa865','INFERENCE INTERFACES','Expose prototype model workflows through usable interfaces.','interface.predict()','runtime',['health-guardian','sentiment']),
    ('spacy','spaCy','#73c9e1','NATURAL LANGUAGE PROCESSING','Explore linguistic structure and practical text representation.','document.parse()','retrieval',[]),
    ('jupyter','Jupyter','#f5a765','RESEARCH WORKFLOWS','Inspect experiments, intermediate artifacts, and notebook implementations.','experiment.inspect()','model',['health-guardian','tactical','qorabot']),
    ('git','Git','#f38570','SOURCE & VERSIONING','Trace changes and inspect publicly available implementation artifacts.','source.diff()','runtime',['health-guardian','amarzero','tactical','qorabot','sentiment']),
    ('linux','Linux','#e7d29a','ENGINEERING ENVIRONMENTS','Work with terminal tooling and model-development environments.','process.execute()','runtime',[]),
    ('mysql','SQL','#89c3d6','STRUCTURED DATA','Explore querying and transformation of structured records.','data.query()','retrieval',[]),
    ('keras','Keras','#ef9393','NEURAL MODEL DEVELOPMENT','Compose neural-network layers for practical learning tasks.','layers.compose()','model',[]),
    ('cplusplus','C++','#6babe6','PROGRAMMING','Express computation through typed systems programming.','compute.step()','runtime',[]),
    ('c','C','#a6bcdc','PROGRAMMING','Explore low-level computation and memory-oriented programming.','memory.inspect()','runtime',[]),
]


def tool_records():
    result = []
    for index, entry in enumerate(TOOLS):
        slug, name, color, category, description, signature, action, projects = entry
        if index < 12:
            angle = -pi/2 + index*2*pi/12
            x, y = 330 + 276*cos(angle), 245 + 194*sin(angle)
        elif index < 18:
            angle = -pi/2 + (index-12)*2*pi/6
            x, y = 330 + 153*cos(angle), 245 + 102*sin(angle)
        else:
            x, y = 330, 245
        result.append(dict(id=slug,name=name,color=color,category=category,description=description,signature=signature,action=action,projects=projects,x=round(x,2),y=round(y,2)))
    return result

GROUPS = {'mooox':'agents','health-guardian':'agents','amarzero':'vision','tactical':'research','qorabot':'research','sentiment':'nlp','healthmeror':'archive'}
DOMAINS = {'mooox':'AGENTIC SECURITY · PRIVATE','health-guardian':'MULTIMODAL SAFETY','amarzero':'VISION × MODEL-BASED RL','tactical':'TACTICAL INTELLIGENCE','qorabot':'SCIENTIFIC RAG','sentiment':'APPLIED NLP','healthmeror':'MEDICAL AI · ARCHIVED'}
SHORT = {'mooox':'Recursive investigation. Sandboxed tools. Evidence-backed findings.','health-guardian':'Perceive. Reason. Verify. Apply a deterministic safety gate.','amarzero':'Visual state estimation meets learned dynamics and tree search.','tactical':'Decode team behavior through multi-layer tactical signals.','qorabot':'Retrieve scientific context. Preserve sources. Generate answers.','sentiment':'Sparse tweet features. Probabilistic classification. Gradio inference.','healthmeror':'Implemented during a competition. No longer running.'}
METRIC_LABELS = {'mooox':'Recursive deepening / architecture scope','health-guardian':'Mocked regression checks / 4 verification tools','amarzero':'Single-object mean error / limited paper experiment','tactical':'Features / clusters · 10-match sample','qorabot':'Cleaned corpus / not a QA accuracy score','sentiment':'Rows before deduplication / source sample','healthmeror':'Past competition project / inactive'}


def glyph(project_id):
    wrapper = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 250" fill="none" aria-hidden="true">'
    if project_id == 'mooox':
        art = '''<g stroke="currentColor" stroke-width="1.1"><path d="m180 29 81 47v93l-81 48-81-48V76Z"/><path d="m180 29v94l81 46M99 76l81 47 81-47M180 123v94"/><path d="m138 67 81 47v93l-81-48V67Z" opacity=".22"/><path d="m53 108 40-23M264 170l43 24M260 78l47-28" stroke-dasharray="3 6"/></g><g class="glyph-pulse" fill="currentColor"><circle cx="99" cy="76" r="4"/><circle cx="261" cy="169" r="4"/><circle cx="180" cy="29" r="4"/></g><g stroke="currentColor" opacity=".4"><rect x="28" y="110" width="37" height="30" rx="4"/><rect x="297" y="37" width="34" height="30" rx="4"/><rect x="298" y="191" width="30" height="30" rx="4"/></g><path d="M169 110v-7a11 11 0 0 1 22 0v7m-25 0h28v23h-28Z" stroke="currentColor" stroke-width="2"/>'''
    elif project_id == 'health-guardian':
        art = '''<path d="M180 25 251 54v76c0 41-71 94-71 94s-71-53-71-94V54Z" fill="currentColor" fill-opacity=".045" stroke="currentColor" stroke-width="1.3"/><path d="m180 43 55 23v64c0 29-55 72-55 72s-55-43-55-72V66Z" stroke="currentColor" opacity=".23"/><path class="glyph-path" d="M42 129h80l16-23 17 48 25-66 22 43 13-16h106" stroke="currentColor" stroke-width="2"/><g stroke="currentColor" opacity=".55"><circle cx="56" cy="58" r="15"/><circle cx="309" cy="65" r="15"/><circle cx="68" cy="206" r="15"/><circle cx="305" cy="204" r="15"/><path d="m70 65 45 8m179 2-54 5m-160 115 42-31m169 29-53-26" stroke-dasharray="3 6"/></g><path d="M304 57v16m-8-8h16M49 58h14" stroke="currentColor" stroke-width="1.8"/>'''
    elif project_id == 'amarzero':
        art = '''<g stroke="currentColor"><circle cx="180" cy="119" r="77" stroke-opacity=".15"/><circle cx="180" cy="119" r="52" stroke-opacity=".4"/><path class="glyph-motion" d="M180 17v22m0 160v22M78 119h22m160 0h22M115 55l15 15m101 99 14 14m-130 0 15-14m101-99 14-15" opacity=".55"/><rect x="139" y="78" width="82" height="82" rx="3" stroke-width="1.7"/><path d="M145 94v-9h10m50 0h9v10m0 47v11h-11m-49 0h-9v-10" stroke-width="3"/><path class="glyph-path" d="M28 190q42-111 102-43t86-57q28-30 87-24" stroke-width="1.1"/><path d="m269 137 24 26m-24-26 34-3m-10 29 20 28m-20-28-21 32" opacity=".5"/></g><g fill="currentColor"><circle cx="180" cy="119" r="5"/><circle cx="269" cy="137" r="3"/><circle cx="293" cy="163" r="3"/><circle cx="303" cy="134" r="3"/><circle cx="313" cy="191" r="3"/></g>'''
    elif project_id == 'tactical':
        art = '''<g transform="translate(180 125) rotate(-12) skewX(9) translate(-180 -125)" stroke="currentColor"><rect x="49" y="39" width="262" height="170" rx="2" fill="currentColor" fill-opacity=".025"/><path d="M180 39v170"/><circle cx="180" cy="124" r="29"/><path d="M49 83h40v85H49m262-85h-40v85h40M49 101h17v49H49m262-49h-17v49h17" opacity=".7"/><path class="glyph-path" d="m80 141 43-53 49 17 48-34 59 38"/><path d="m117 164 50-36 67 35" opacity=".3"/><g fill="currentColor"><circle cx="80" cy="141" r="5"/><circle cx="123" cy="88" r="5"/><circle cx="172" cy="105" r="5"/><circle cx="220" cy="71" r="5"/><circle cx="279" cy="109" r="5"/></g><g fill="currentColor" opacity=".4"><circle cx="116" cy="164" r="4"/><circle cx="166" cy="128" r="4"/><circle cx="234" cy="164" r="4"/><circle cx="97" cy="117" r="4"/><circle cx="247" cy="126" r="4"/></g></g>'''
    elif project_id == 'qorabot':
        art = '''<g stroke="currentColor"><circle cx="173" cy="124" r="54" fill="currentColor" fill-opacity=".04"/><ellipse class="glyph-motion" cx="180" cy="125" rx="126" ry="37" transform="rotate(-24 180 125)"/><circle cx="173" cy="124" r="85" stroke-dasharray="2 8" opacity=".3"/><path d="m134 101 45-12 28 37-51 15Z" opacity=".55"/><path d="m145 151 25-40 39-8" opacity=".3"/><rect x="279" y="34" width="38" height="52" rx="3"/><path d="M287 48h22m-22 10h22m-22 10h14m-30-4-38 20" opacity=".4"/><rect x="34" y="169" width="38" height="52" rx="3"/><path d="M42 183h22m-22 10h22m-22 10h14m17-22 35-25" opacity=".4"/></g><g class="glyph-pulse" fill="currentColor"><circle cx="280" cy="103" r="4"/><circle cx="75" cy="159" r="4"/><circle cx="196" cy="92" r="3"/></g>'''
    elif project_id == 'sentiment':
        art = '''<g stroke="currentColor"><rect x="74" y="62" width="208" height="128" rx="12" fill="currentColor" fill-opacity=".03"/><path d="m121 190-13 22 44-22"/><path class="glyph-path" d="M30 123h66l12-32 18 64 20-48 16 18h51l12-25 13 43 19-20h72" stroke-width="1.4"/><path d="M101 76h157M102 175h157" opacity=".15"/><path d="M98 123V99m14 24V89m14 34v-12m14 12v30m14-30v40m14-40v20m14-20v-7m14 7V94m14 29V78m14 45V96m14 27v27m14-27v40m14-40v14" stroke-width="3" opacity=".4"/><circle cx="318" cy="74" r="20"/><path d="M310 74h16m-8-8v16"/><circle cx="40" cy="188" r="14"/><path d="M34 188h12"/></g>'''
    else:
        art = '''<path d="M180 188s-89-56-89-108c0-49 65-58 89-10 24-48 89-39 89 10 0 52-89 108-89 108Z" stroke="currentColor" stroke-width="1.3" opacity=".65"/><path d="M105 113h40l15-24 21 47 13-23h61" stroke="currentColor" opacity=".65"/><g stroke="currentColor" opacity=".25"><circle cx="180" cy="125" r="103" stroke-dasharray="2 9"/><path d="M68 75 180 24l110 53m0 98-110 49-112-48"/></g>'''
    return wrapper + art + '</svg>'

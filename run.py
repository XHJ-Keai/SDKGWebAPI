from flask import Flask, jsonify, request
from flask_cors import CORS
from sckg.graph import SoftwareKG

from util.log_util import LogUtil
from util.path_util import PathUtil

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
graph_path = PathUtil.graph_data("KG", "V1.0.0")
tree = PathUtil.trie("Trie", "V1.0.0")
sckg = SoftwareKG(graph_path, tree)
log = LogUtil.get_log_util()


@app.route('/')
def hello_world():
    return 'Hello World~'


@app.route('/get_node_by_concepts/', methods=["GET", "POST"])
def get_node_by_concepts():
    concepts = request.json['concepts']
    log.log_call_interface(concepts)
    result = dict()
    for concept in concepts:
        property_dict = {
            'concept_name': sckg.get_node_by_concept(concept)[0]['properties']['concept_name'],
            'score': sckg.get_node_by_concept(concept)[0]['properties']['score']
        }
        result[concept] = {
            'id': sckg.get_node_by_concept(concept)[0]['id'],
            'properties': property_dict,
            'label': list(sckg.get_node_by_concept(concept)[0]['labels'])
        }
    return jsonify(result)


@app.route('/get_node_by_ids/', methods=["GET", "POST"])
def get_node_by_ids():
    ids = request.json['ids']
    log.log_call_interface(ids)
    result = dict()
    for id in ids:
        property_dict = {
            'concept_name': sckg.get_node_info_by_id(id)['properties']['concept_name'],
            'score': sckg.get_node_info_by_id(id)['properties']['score']
        }
        result[id] = {
            'id': sckg.get_node_info_by_id(id)['id'],
            'properties': property_dict,
            'label': list(sckg.get_node_info_by_id(id)['labels'])
        }
    return jsonify(result)


@app.route('/get_concept_from_sentence/', methods=["GET", "POST"])
def get_concept_from_sentence():
    result = dict()
    sentences = request.json['sentences']
    log.log_call_interface(sentences)
    for sentence in sentences:
        result[sentence] = list(sckg.find_all_concept_from_sentence(sentence))
    return jsonify(result)


@app.route('/find_include_prefix_concepts/', methods=["GET", "POST"])
def find_include_prefix_concepts():
    result = dict()
    concepts = request.json['concepts']
    log.log_call_interface(concepts)
    for concept in concepts:
        result[concept] = list(sckg.find_include_prefix_concept(concept))
    return jsonify(result)


@app.route('/get_concept_categories/', methods=["GET", "POST"])
def get_concept_categories():
    concepts = request.json['concepts']
    log.log_call_interface(concepts)
    result = dict()
    for concept in concepts:
        result[concept] = sckg.get_upper_concept(concept)
    return jsonify(result)


@app.route('/get_common_concept_categories/', methods=["GET", "POST"])
def get_common_concept_categories():
    concepts = request.json['concepts']
    result = dict()
    log.log_call_interface(concepts)
    result['categories'] = sckg.get_common_upper_concept(concepts[0], concepts[1])
    return jsonify(result)


@app.route('/get_included_concepts/', methods=["GET", "POST"])
def get_included_concepts():
    concepts = request.json['concepts']
    result = dict()
    log.log_call_interface(concepts)
    for concept in concepts:
        result[concept] = sckg.find_in_is_a_relation_concept(concept)
    return jsonify(result)


if __name__ == '__main__':
    app.run()

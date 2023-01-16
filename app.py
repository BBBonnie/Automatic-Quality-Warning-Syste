from flask import Flask, request, make_response, jsonify
import dbQuery

app = Flask(__name__)


@app.after_request
def after(resp):
    resp = make_response(resp)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'GET,POST'
    resp.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'

    return resp


@app.route('/')
def index():
    return make_response()


@app.route('/components')
def components():
    is_need_sort = request.args.get("is_sorted")
    response = dbQuery.listComponents()
    if is_need_sort is True:
        sorted_resp = sorted(response['response'], key=lambda student: student[4])
        response = {'response': sorted_resp, 'msg': "done"}

    return make_response(jsonify(resp=response))


@app.route('/addComponent', methods=["GET", "POST"])
def addComponent():
    req_data = request.get_json()
    component_name = req_data['componentName']
    component_contact = req_data['componentContact']
    component_manufacturer = req_data['componentManufacturer']
    component_failure_rate = req_data['componentFailureRate']
    component_price = req_data['componentPrice']
    component_quantity = req_data['componentQuantity']
    print(req_data)

    dbQuery.addComponents(component_name, component_contact, component_manufacturer,
                          component_failure_rate, component_price, component_quantity)
    response = dbQuery.listComponents()
    print(response)
    return make_response(jsonify(resp=response))


@app.route('/updateComponent', methods=["GET", "POST"])
def update_component():
    req_data = request.get_json()
    component_id = req_data['updatedID']
    component_name = req_data['updatedName']
    component_contact = req_data['updatedContact']
    component_manufacturer = req_data['updatedManu']
    component_failure_rate = req_data['updatedFR']
    component_price = req_data['updatedPrice']
    component_quantity = req_data['updatedQuantity']

    dbQuery.update_components(component_id, component_name, component_contact, component_manufacturer,
                              component_failure_rate, component_price, component_quantity)
    response = dbQuery.listComponents()

    return make_response(jsonify(resp=response))


@app.route('/removeComponent', methods=["GET", "POST"])
def removeComponent():
    req_data = request.get_json()
    print(req_data)
    component_id = req_data['deletedID']
    msg = dbQuery.removeComponent(component_id)
    response = dbQuery.listComponents()
    return make_response(jsonify(resp=response))


@app.route('/failmodes')
def failmodes():
    response = dbQuery.listFailmodes()
    return make_response(jsonify(resp=response))


@app.route('/addFailmode', methods=["GET", "POST"])
def addFailmode():
    req_data = request.get_json()
    failmode_name = req_data['failModeName']
    failmode_code = req_data['failCode']

    print(req_data)

    dbQuery.addFailMode(failmode_name, failmode_code)
    response = dbQuery.listFailmodes()
    # print(response)
    return make_response(jsonify(resp=response))


@app.route('/updateFailmode', methods=["GET", "POST"])
def update_failmode():
    req_data = request.get_json()
    failmode_id = req_data['updatedID']
    failmode_name = req_data['updatedName']
    failmode_code = req_data['updatedCode']

    dbQuery.update_failmode(failmode_id, failmode_name, failmode_code)
    response = dbQuery.listFailmodes()

    return make_response(jsonify(resp=response))


@app.route('/removeFailmode', methods=["GET", "POST"])
def removeFailmode():
    req_data = request.get_json()
    fm_id = req_data['deletedID']
    msg = dbQuery.removeFailMode(fm_id)
    response = dbQuery.listFailmodes()
    return make_response(jsonify(resp=response))


@app.route('/mappings')
def mappings():
    mp_response = dbQuery.listMappings()
    return make_response(jsonify(resp=mp_response))


@app.route('/addMapping', methods=["GET", "POST"])
def addMapping():
    req_data = request.get_json()
    fail_code = req_data['failCode']
    componentID = req_data['component']
    fail_modeID = req_data['failMode']
    print(req_data)

    # dbQuery.addMapping(fail_code, component, fail_mode)
    response = dbQuery.listMappings()
    # print(response)
    return make_response(jsonify(resp=response))


@app.route('/removeMapping', methods=["GET", "POST"])
def removeMapping():
    req_data = request.get_json()
    print(req_data)
    mapping_id = req_data['deletedID']
    msg = dbQuery.removeMapping(mapping_id)
    response = dbQuery.listMappings()
    return make_response(jsonify(resp=response))

# def partition(arr, low, high):
#     i = (low - 1)  # index of smaller element
#
#     pivot = arr[high][4]  # pivot
#
#     for j in range(low, high):
#
#         # If current element is smaller than or
#         # equal to pivot
#         if arr[j][4] <= pivot:
#             # increment index of smaller element
#             i = i + 1
#             arr[i], arr[j] = arr[j], arr[i]
#
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return i + 1
#
#
# def quickSort(arr, low, high):
#     if len(arr) == 1:
#         return arr
#     if low < high:
#         # pi is partitioning index, arr[p] is now
#         # at right place
#         pi = partition(arr, low, high)
#
#         # Separately sort elements before
#         # partition and after partition
#         quickSort(arr, low, pi - 1)
#         quickSort(arr, pi + 1, high)

def partition(array, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot



def quicksort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    def _quicksort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        _quicksort(array, begin, pivot-1)
        _quicksort(array, pivot+1, end)
    return _quicksort(array, begin, end)

if __name__ == '__main__':
    app.run()

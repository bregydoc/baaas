from ariadne import load_schema_from_path, QueryType, MutationType, ScalarType, make_executable_schema, upload_scalar


query = QueryType()
mutation = MutationType()
datetime_scalar = ScalarType("Datetime")


@datetime_scalar.serializer
def serialize_datetime(value):
    return value.isoformat()


@query.field("live")
def resolve_live(_, info) -> str:
    # request = info.context["request"]
    # print(request)
    print(info)
    return "ok"


@query.field("process")
def resolve_process(_, info) -> str:
    request = info.context["request"]
    print(request)
    return "ok"


@mutation.field("registerNewEvidence")
def resolve_register_new_evidence(_, info) -> str:
    request = info.context["request"]
    print(request)
    return "ok"


type_defs = load_schema_from_path("./api/schema/schema.graphqls")

schema = make_executable_schema(
    type_defs, query,  mutation, upload_scalar)

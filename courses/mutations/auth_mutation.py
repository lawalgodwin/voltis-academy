import graphene
import graphql_jwt

from courses.mutations.user_mutation import CreateUser


class AuthMutation(graphene.ObjectType):
    register = CreateUser.Field()
    sign_in = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    log_out = graphql_jwt.Revoke.Field()

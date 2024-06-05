import graphene
from users.schema import Query as UsersQuery, Mutation as UsersMutation
from profiles.schema import Query as ProfilesQuery, Mutation as ProfilesMutation
from reqs.schema import Query as RequestsQuery, Mutation as RequestsMutation
from payments.schema import Query as PaymentsQuery, Mutation as PaymentsMutation
from reviews.schema import Query as ReviewsQuery, Mutation as ReviewsMutation
from media.schema import Query as MediaQuery, Mutation as MediaMutation
from orders.schema import Query as OrdersQuery, Mutation as OrdersMutation
from complaints.schema import Query as ComplaintsQuery, Mutation as ComplaintsMutation
from otp.schema import Query as OTPQuery, Mutation as OTPMutation
from notifications.schema import Query as NotificationsQuery, Mutation as NotificationsMutation
from support_tickets.schema import Query as SupportTicketsQuery, Mutation as SupportTicketsMutation
from roles.schema import Query as RolesQuery, Mutation as RolesMutation
from live_location.schema import Query as LiveLocationQuery, Mutation as LiveLocationMutation
from cars.schema import Query as CarsQuery, Mutation as CarsMutation
from cities.schema import Query as CitiesQuery, Mutation as CitiesMutation
from services.schema import Query as ServicesQuery, Mutation as ServicesMutation
from achievements.schema import Query as AchievementsQuery, Mutation as AchievementsMutation
from certificates.schema import Query as CertificatesQuery, Mutation as CertificatesMutation
from blog_posts.schema import Query as BlogPostsQuery, Mutation as BlogPostsMutation
from faqs.schema import Query as FAQsQuery, Mutation as FAQsMutation
from transactions.schema import Query as TransactionsQuery, Mutation as TransactionsMutation


class Query(
    UsersQuery, ProfilesQuery, RequestsQuery, PaymentsQuery, ReviewsQuery,
    MediaQuery, OrdersQuery, ComplaintsQuery, OTPQuery, NotificationsQuery,
    SupportTicketsQuery, RolesQuery, LiveLocationQuery, CarsQuery, CitiesQuery,
    ServicesQuery, AchievementsQuery, CertificatesQuery, BlogPostsQuery, FAQsQuery,
    TransactionsQuery, graphene.ObjectType
):
    pass


class Mutation(
    UsersMutation, ProfilesMutation, RequestsMutation, PaymentsMutation, ReviewsMutation,
    MediaMutation, OrdersMutation, ComplaintsMutation, OTPMutation, NotificationsMutation,
    SupportTicketsMutation, RolesMutation, LiveLocationMutation, CarsMutation, CitiesMutation,
    ServicesMutation, AchievementsMutation, CertificatesMutation, BlogPostsMutation, FAQsMutation,
    TransactionsMutation, graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)

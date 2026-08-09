// ============================================================
// C4 Model — Arquitetura Segura da Plataforma Yummers
// Tecnologia utilizda: https://structurizr.com/
// Documentação da DSL utilizada: https://docs.structurizr.com/dsl
// Para gerar o diagrama: https://playground.structurizr.com/
// ============================================================

workspace "Yummers — Arquitetura Segura" "Modelagem C4 da arquitetura segura da plataforma Yummers." {

    model {

        // ============================================================
        // PESSOAS
        // ============================================================

        cliente = person "Cliente" {
            description "Busca, pede, paga, acompanha e avalia pedidos."
        }

        entregador = person "Entregador" {
            description "Aceita rotas, atualiza localização e confirma coleta e entrega."
        }

        estabelecimento = person "Estabelecimento" {
            description "Gerencia cardápio, preparo e repasses."
        }

        administrador = person "Administrador" {
            description "Aprova cadastros, audita e monitora a plataforma."
        }


        // ============================================================
        // PLATAFORMA YUMMERS
        // ============================================================

        yummers = softwareSystem "Plataforma Yummers" {

            // --------------------------------------------------------
            // INTERFACES
            // --------------------------------------------------------

            mobile = container "Aplicativo Mobile" {
                technology "iOS / Android"
                description "Interface utilizada por Clientes e Entregadores."
                tags "MobileApp"
            }

            portal = container "Portal Web" {
                technology "Web Application"
                description "Interface utilizada por Estabelecimentos e Administradores."
                tags "WebApp"
            }


            // --------------------------------------------------------
            // BACKEND
            // --------------------------------------------------------

            api = container "API do Sistema" {
                technology "REST / HTTPS"
                description "Implementa as regras de negócio e orquestra pedidos, pagamentos, entregas, notificações e repasses. Recalcula e valida no servidor os valores recebidos do cliente antes de processá-los."
                tags "Backend"
            }


            // --------------------------------------------------------
            // AUTORIZAÇÃO
            // --------------------------------------------------------

            autorizacao = container "Autorização" {
                technology "Middleware"
                description "Verifica a autoridade sobre o recurso solicitado (RS03) e a permissão para executar a operação (RS04)."
                tags "AuthorizationService"
            }


            // --------------------------------------------------------
            // BANCO DE DADOS
            // --------------------------------------------------------

            db = container "Banco de Dados" {
                technology "SQL"
                description "Armazena dados cadastrais, financeiros, catálogos, pedidos, histórico, permissões e registros de auditoria."
                tags "Database"
            }


            // --------------------------------------------------------
            // AUDITORIA / MONITORAMENTO
            // --------------------------------------------------------

            logs = container "Logs de Auditoria" {
                technology "Append-only"
                description "Registra operações sensíveis, tentativas de acesso não autorizado, pagamentos, estornos, alterações relevantes e liberação de repasses. Os registros são protegidos contra alteração e exclusão."
                tags "AuditLog"
            }
        }


        // ============================================================
        // SERVIÇOS EXTERNOS
        // ============================================================

        autenticacao = softwareSystem "Serviço de Autenticação" {
            description "Serviço externo responsável por validar credenciais e exigir reautenticação ou segundo fator antes de operações sensíveis. Controle RS01."
            tags "SecurityService"
        }

        pagamento = softwareSystem "Gateway de Pagamento" {
            description "Serviço externo responsável por cobranças, custódia, estornos e repasses."
            tags "PaymentService"
        }

        notificacao = softwareSystem "Serviço de Notificações" {
            description "Serviço externo responsável pelo envio de notificações push, e-mails e atualizações de status."
            tags "NotificationService"
        }

        geolocalizacao = softwareSystem "Serviço de Geolocalização" {
            description "Serviço externo responsável por mapas, rotas e rastreamento em tempo real."
            tags "LocationService"
        }


        // ============================================================
        // USUÁRIOS → INTERFACES
        // ============================================================

        cliente -> mobile "Utiliza" "HTTPS / TLS"
        entregador -> mobile "Utiliza" "HTTPS / TLS"
        estabelecimento -> portal "Utiliza" "HTTPS / TLS"
        administrador -> portal "Utiliza" "HTTPS / TLS"


        // ============================================================
        // INTERFACES → API
        // ============================================================

        mobile -> api "Realiza requisições" "HTTPS + token de sessão"
        portal -> api "Realiza requisições" "HTTPS + token de sessão"


        // ============================================================
        // AUTENTICAÇÃO — RS01
        // ============================================================

        api -> autenticacao "Valida credenciais e tokens e solicita reautenticação em operações sensíveis" "HTTPS [RS01]"


        // ============================================================
        // AUTORIZAÇÃO — RS03 / RS04
        // ============================================================

        api -> autorizacao "Solicita validação de acesso antes de executar operações" "Chamada interna [RS03 / RS04]"

        autorizacao -> db "Consulta proprietário do recurso, role e permissões" "SQL [RS03 / RS04]"


        // ============================================================
        // AUDITORIA / MONITORAMENTO
        // ============================================================

        api -> logs "Registra operações sensíveis, falhas de autorização e eventos relevantes" "Interno [RS01 / RS03 / RS04]"

        autorizacao -> logs "Registra tentativas de acesso não autorizado" "Interno [RS03 / RS04]"

        logs -> db "Persiste registros de auditoria protegidos contra alteração e exclusão" "SQL"


        // ============================================================
        // PAGAMENTO
        // ============================================================

        api -> pagamento "Processa cobranças, custódia, estornos e repasses" "HTTPS"


        // ============================================================
        // NOTIFICAÇÕES
        // ============================================================

        api -> notificacao "Envia atualizações de pedidos e operações" "HTTPS"


        // ============================================================
        // GEOLOCALIZAÇÃO
        // ============================================================

        api -> geolocalizacao "Consulta rotas e rastreamento em tempo real" "HTTPS"
    }


    // =================================================================
    // VIEWS
    // =================================================================

    views {

        // ============================================================
        // CONTEXTO DO SISTEMA
        // ============================================================

        systemContext yummers "SystemContext" {
            include cliente
            include entregador
            include estabelecimento
            include administrador

            include yummers

            include autenticacao
            include pagamento
            include notificacao
            include geolocalizacao

            autolayout lr

            title "Yummers — Contexto do Sistema"
        }


        // ============================================================
        // DIAGRAMA DE ARQUITETURA SEGURA
        // ============================================================

        container yummers "SecureArchitecture" {
            include cliente
            include entregador
            include estabelecimento
            include administrador

            include mobile
            include portal
            include api
            include autorizacao
            include db
            include logs

            include autenticacao
            include pagamento
            include notificacao
            include geolocalizacao

            autolayout lr

            title "Yummers — Diagrama da Arquitetura Segura (C4 — Containers)"
        }


        // ============================================================
        // ESTILOS
        // ============================================================

        styles {

            // --------------------------------------------------------
            // PESSOAS
            // --------------------------------------------------------

            element "Person" {
                shape person
                background #084C61
                color #FFFFFF
            }


            // --------------------------------------------------------
            // SOFTWARE SYSTEM
            // --------------------------------------------------------

            element "Software System" {
                shape roundedBox
                background #4A5568
                color #FFFFFF
            }


            // --------------------------------------------------------
            // SERVIÇO DE AUTENTICAÇÃO
            // --------------------------------------------------------

            element "SecurityService" {
                shape component
                background #8E44AD
                color #FFFFFF
                border solid
            }


            // --------------------------------------------------------
            // SERVIÇO DE AUTORIZAÇÃO
            // --------------------------------------------------------

            element "AuthorizationService" {
                shape diamond
                background #D35400
                color #FFFFFF
                border solid
            }


            // --------------------------------------------------------
            // GATEWAY DE PAGAMENTO
            // --------------------------------------------------------

            element "PaymentService" {
                shape component
                background #2471A3
                color #FFFFFF
                border solid
            }


            // --------------------------------------------------------
            // SERVIÇO DE NOTIFICAÇÕES
            // --------------------------------------------------------

            element "NotificationService" {
                shape component
                background #B9770E
                color #FFFFFF
                border solid
            }


            // --------------------------------------------------------
            // SERVIÇO DE GEOLOCALIZAÇÃO
            // --------------------------------------------------------

            element "LocationService" {
                shape component
                background #148F77
                color #FFFFFF
                border solid
            }


            // --------------------------------------------------------
            // CONTAINERS
            // --------------------------------------------------------

            element "Container" {
                background #4381C4
                color #FFFFFF
            }


            // --------------------------------------------------------
            // BACKEND
            // --------------------------------------------------------

            element "Backend" {
                shape roundedBox
                background #2E6F95
                color #FFFFFF
            }


            // --------------------------------------------------------
            // APLICATIVO MOBILE
            // --------------------------------------------------------

            element "MobileApp" {
                shape mobileDevicePortrait
                background #4381C4
                color #FFFFFF
            }


            // --------------------------------------------------------
            // APLICAÇÃO WEB
            // --------------------------------------------------------

            element "WebApp" {
                shape webBrowser
                background #4381C4
                color #FFFFFF
            }


            // --------------------------------------------------------
            // BANCO DE DADOS
            // --------------------------------------------------------

            element "Database" {
                shape cylinder
                background #356B83
                color #FFFFFF
            }


            // --------------------------------------------------------
            // LOGS DE AUDITORIA
            // --------------------------------------------------------

            element "AuditLog" {
                shape pipe
                background #397D5A
                color #FFFFFF
            }
        }
    }
}
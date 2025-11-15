import dns.resolver


class ResolverDNS:
    def dnsbruto():
        res = dns.resolver.Resolver()
        alvo = input("Informe: ")


        try: 
            resultado = res.resolve(alvo, "A")

            for info in resultado:
                print(alvo, "->", info)
        except:
            pass

if __name__ == "__main__":
        brute = ResolverDNS()
        brute.dnsbruto()



import json
import datetime
from jwcrypto import jwk

def generate_jwk():
    """
    Generate an elliptic curve key (secp256k1) using JWK.
    """
    key = jwk.JWK.generate(kty='EC', crv='secp256k1')
    return key

def export_public_jwk(key):
    """
    Export the public portion of the JWK as a dictionary.
    """
    return key.export_public(as_dict=True)

def create_did_document(did: str, public_jwk: dict, also_known_as: list = None) -> dict:
    """
    Create a basic DID Document using the JWK for public key representation.
    The document includes an authentication section and an alsoKnownAs field.
    """
    return {
        "@context": "https://www.w3.org/ns/did/v1",
        "id": did,
        "authentication": [{
            "id": f"{did}#keys-1",
            "type": "EcdsaSecp256k1VerificationKey2019",
            "controller": did,
            "publicKeyJwk": public_jwk
        }],
        "alsoKnownAs": also_known_as if also_known_as is not None else []
    }

def main():
    # Generate key pair for the old DID (DID_01)
    old_key = generate_jwk()
    old_pub_jwk = export_public_jwk(old_key)
    
    # Generate key pair for the new DID (DID_02)
    new_key = generate_jwk()
    new_pub_jwk = export_public_jwk(new_key)
    
    # Define our DIDs (using simple names for the PoC)
    did_old = "DID_01"
    did_new = "DID_02"
    
    # Create initial DID Documents with a baseline external reference
    doc_old = create_did_document(did_old, old_pub_jwk, also_known_as=["did:example:ext01"])
    doc_new = create_did_document(did_new, new_pub_jwk, also_known_as=["did:example:ext02"])
    
    # Append a timestamp to the alsoKnownAs field to simulate dynamic cross-referencing
    timestamp = datetime.datetime.utcnow().isoformat() + "Z"
    doc_old["alsoKnownAs"].append(f"timestamp:{timestamp}")
    doc_new["alsoKnownAs"].append(f"timestamp:{timestamp}")
    
    # Output the DID Documents in JSON format
    print("DID Document for DID_01 (old):")
    print(json.dumps(doc_old, indent=4))
    print("\nDID Document for DID_02 (new):")
    print(json.dumps(doc_new, indent=4))

if __name__ == "__main__":
    main()
